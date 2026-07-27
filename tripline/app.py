import math
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = "database.db"

# --- Efficiency scale, shared by the dashboard gauge and the per-row bars ---
GAUGE_MAX = 22          # km/l considered "top of scale" for the dial
GAUGE_GOOD = 16
GAUGE_AVERAGE = 13


def gauge_point(value, radius, cx=110, cy=110, max_value=GAUGE_MAX):
    """Return the (x, y) on the semicircle dial for a given efficiency value."""
    t = max(0, min(value / max_value, 1))
    phi = math.radians(180 - 180 * t)
    x = cx + radius * math.cos(phi)
    y = cy - radius * math.sin(phi)
    return round(x, 1), round(y, 1)


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS records(
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_no TEXT,
        trip_date TEXT,
        start_km INTEGER,
        end_km INTEGER,
        distance REAL,
        fuel_litres REAL,
        driver TEXT,
        efficiency REAL,
        status TEXT,
        remarks TEXT,
        UNIQUE(vehicle_no, trip_date)
    )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():

    conn = get_db()

    search = request.args.get("search", "")
    vehicle = request.args.get("vehicle", "")
    flash = request.args.get("flash", "")

    query = "SELECT * FROM records WHERE 1=1"
    params = []

    if search:
        query += """
        AND (
            vehicle_no LIKE ?
            OR driver LIKE ?
        )
        """
        params.extend([
            f"%{search}%",
            f"%{search}%"
        ])

    if vehicle:
        query += " AND vehicle_no=?"
        params.append(vehicle)

    query += " ORDER BY record_id DESC"

    records = conn.execute(query, params).fetchall()

    vehicles = conn.execute("""
        SELECT DISTINCT vehicle_no
        FROM records
        ORDER BY vehicle_no
    """).fetchall()

    conn.close()

    total_records = len(records)

    # Fuel + efficiency stats now reflect the current filtered view,
    # matching total_records instead of always summing the whole table.
    total_fuel = sum(r["fuel_litres"] for r in records) if records else 0
    efficiencies = [r["efficiency"] for r in records if r["efficiency"] is not None]
    avg_efficiency = round(sum(efficiencies) / len(efficiencies), 2) if efficiencies else 0
    fleet_count = len(vehicles)

    needle_x, needle_y = gauge_point(avg_efficiency, radius=70)

    return render_template(
        "index.html",
        records=records,
        vehicles=vehicles,
        total_records=total_records,
        total_fuel=round(total_fuel, 2),
        avg_efficiency=avg_efficiency,
        fleet_count=fleet_count,
        needle_x=needle_x,
        needle_y=needle_y,
        gauge_good=GAUGE_GOOD,
        gauge_average=GAUGE_AVERAGE,
        gauge_max=GAUGE_MAX,
        search=search,
        vehicle=vehicle,
        flash=flash
    )


@app.route("/add", methods=["GET", "POST"])
def add_record():

    if request.method == "POST":

        vehicle_no = request.form["vehicle_no"]
        trip_date = request.form["trip_date"]
        start_km = int(request.form["start_km"])
        end_km = int(request.form["end_km"])
        fuel_litres = float(request.form["fuel_litres"])
        driver = request.form["driver"]
        remarks = request.form["remarks"]

        if end_km <= start_km:
            return render_template(
                "error.html",
                message="End KM must be greater than Start KM."
            )

        if fuel_litres <= 0:
            return render_template(
                "error.html",
                message="Fuel litres must be greater than zero."
            )

        distance = end_km - start_km
        efficiency = round(distance / fuel_litres, 2)

        if efficiency >= GAUGE_GOOD:
            status = "Good"
        elif efficiency >= GAUGE_AVERAGE:
            status = "Average"
        else:
            status = "Poor"

        conn = get_db()

        try:

            conn.execute("""
            INSERT INTO records(
                vehicle_no,
                trip_date,
                start_km,
                end_km,
                distance,
                fuel_litres,
                driver,
                efficiency,
                status,
                remarks
            )
            VALUES(?,?,?,?,?,?,?,?,?,?)
            """,
            (
                vehicle_no,
                trip_date,
                start_km,
                end_km,
                distance,
                fuel_litres,
                driver,
                efficiency,
                status,
                remarks
            ))

            conn.commit()
            conn.close()

            return redirect("/?flash=logged")

        except sqlite3.IntegrityError:

            conn.close()

            return render_template(
                "error.html",
                message="A record for this vehicle and date already exists."
            )

    return render_template(
        "form.html",
        record=None,
        gauge_good=GAUGE_GOOD,
        gauge_average=GAUGE_AVERAGE
    )

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_record(id):

    conn = get_db()

    record = conn.execute(
        "SELECT * FROM records WHERE record_id=?",
        (id,)
    ).fetchone()

    if not record:
        conn.close()
        return render_template("not_found.html")

    if request.method == "POST":

        vehicle_no = request.form["vehicle_no"]
        trip_date = request.form["trip_date"]
        start_km = int(request.form["start_km"])
        end_km = int(request.form["end_km"])
        fuel_litres = float(request.form["fuel_litres"])
        driver = request.form["driver"]
        remarks = request.form["remarks"]

        if end_km <= start_km:
            conn.close()
            return render_template(
                "error.html",
                message="End KM must be greater than Start KM."
            )

        if fuel_litres <= 0:
            conn.close()
            return render_template(
                "error.html",
                message="Fuel litres must be greater than zero."
            )

        distance = end_km - start_km
        efficiency = round(distance / fuel_litres, 2)

        if efficiency >= GAUGE_GOOD:
            status = "Good"
        elif efficiency >= GAUGE_AVERAGE:
            status = "Average"
        else:
            status = "Poor"

        conn.execute("""
UPDATE records
SET
    vehicle_no=?,
    trip_date=?,
    start_km=?,
    end_km=?,
    distance=?,
    fuel_litres=?,
    driver=?,
    efficiency=?,
    status=?,
    remarks=?
WHERE record_id=?
""",
(
    vehicle_no,
    trip_date,
    start_km,
    end_km,
    distance,
    fuel_litres,
    driver,
    efficiency,
    status,
    remarks,
    id
))

        conn.commit()
        conn.close()

        return redirect("/?flash=updated")

    conn.close()

    return render_template(
        "form.html",
        record=record,
        gauge_good=GAUGE_GOOD,
        gauge_average=GAUGE_AVERAGE
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html"), 404


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
