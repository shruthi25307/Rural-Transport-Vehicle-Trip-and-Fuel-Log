import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
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

# Clear existing data so re-running this script doesn't duplicate rows
cursor.execute("DELETE FROM records")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='records'")

data = [
("TN01AB1234","2025-07-01",15000,15120,120,8,"Ravi",15.00,"Average","Regular delivery"),
("TN01AB1234","2025-07-03",15120,15260,140,9,"Ravi",15.56,"Good","On-time trip"),
("TN02CD5678","2025-07-01",22000,22180,180,12,"Suresh",15.00,"Average","City transport"),
("TN03EF9012","2025-07-02",18000,18150,150,11,"Mohan",13.64,"Average","Traffic delay"),
("TN04GH3456","2025-07-03",9000,9120,120,7,"Kumar",17.14,"Good","Efficient route"),
("TN05IJ7890","2025-07-02",30000,30180,180,13,"Ravi",13.85,"Average","Routine service"),
("TN06KL1122","2025-07-01",12000,12100,100,6,"Arun",16.67,"Good","Morning delivery"),
("TN07MN3344","2025-07-02",45000,45160,160,12,"Ramesh",13.33,"Average","Heavy traffic"),
("TN09QR7788","2018-01-10",8000,8150,150,10,"Vijay",15.00,"Average","Old record"),
("TN10ST9900","2025-07-07",10000,10150,150,20,"Ajay",7.50,"Poor","High fuel usage"),
("TN11UV1357","2025-07-04",20000,20200,200,10,"Ravi",20.00,"Good","Excellent trip"),
("TN12WX2468","2025-07-04",35000,35140,140,9,"Suresh",15.56,"Good","Smooth journey"),
("TN13YZ3579","2025-07-05",5000,5130,130,10,"Mohan",13.00,"Average","Minor delay"),
("TN14AA4680","2025-07-05",17000,17160,160,8,"Kumar",20.00,"Good","Fast delivery"),
("TN15BB5791","2025-07-06",25000,25110,110,10,"Arun",11.00,"Poor","Extra stops"),
("TN16CC6802","2025-07-06",40000,40190,190,11,"Ramesh",17.27,"Good","High efficiency"),
("TN17DD7913","2025-07-07",13000,13140,140,10,"Karthik",14.00,"Average","Regular route"),
("TN18EE8024","2025-07-08",28000,28170,170,12,"Vijay",14.17,"Average","Customer visit"),
("TN19FF9135","2025-07-08",6000,6100,100,9,"Ajay",11.11,"Poor","Fuel issue"),
("TN20GG0246","2025-07-09",19000,19220,220,11,"Ravi",20.00,"Good","Best performance")
]
cursor.executemany("""
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
""", data)

conn.commit()

count = cursor.execute(
    "SELECT COUNT(*) FROM records"
).fetchone()[0]

print("Inserted:", count)

conn.close()