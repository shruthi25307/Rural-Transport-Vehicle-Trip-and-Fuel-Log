import sqlite3

conn = sqlite3.connect("database.db")

rows = conn.execute("""
SELECT record_id, efficiency
FROM records
""").fetchall()

for row in rows:

    record_id = row[0]
    efficiency = row[1]

    if efficiency >= 16:
        status = "Good"
    elif efficiency >= 13:
        status = "Average"
    else:
        status = "Poor"

    conn.execute("""
    UPDATE records
    SET status=?
    WHERE record_id=?
    """, (status, record_id))

conn.commit()
conn.close()

print("Status updated successfully!")