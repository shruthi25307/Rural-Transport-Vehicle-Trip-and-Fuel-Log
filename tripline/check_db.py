import sqlite3

conn = sqlite3.connect("database.db")

try:
    rows = conn.execute("SELECT * FROM records").fetchall()

    print("Number of rows:", len(rows))

    for row in rows[:5]:
        print(row)

except Exception as e:
    print("ERROR:", e)

conn.close()