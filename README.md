# 🚛 Rural Transport Vehicle Trip & Fuel Log

🌐 **Live Demo:** https://rural-transport-vehicle-trip-and-fuel-log.onrender.com/
**LEVEL 2:** https://rural-transport-vehicle-trip-and-fuel.onrender.com/

## 🎥 Demo Video

[Download / View the Demo Video](https://github.com/shruthi25307/Rural-Transport-Vehicle-Trip-and-Fuel-Log/blob/main/SIH_2026.mp4)

---

## Problem Statement

Rural transport operators often record vehicle trips and fuel purchases manually in registers. As a result, fuel efficiency is rarely calculated, making it difficult to identify vehicle performance issues or unusual fuel consumption.

This application records trip and fuel data, automatically calculates vehicle efficiency, and helps transport in-charges monitor vehicle performance over time.

---

## Features

- Add new trip records
- Update existing records
- Search records by vehicle number or driver
- Filter records by vehicle
- Automatic fuel efficiency calculation
- Vehicle status monitoring (Good / Average / Poor)
- Dark and Light mode support
- Responsive design for mobile and desktop
- SQLite database storage

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** SQLite
- **Deployment:** Render

---

## Installation & Running

### 1. Clone the repository

```bash
git clone https://github.com/shruthi25307/Rural-Transport-Vehicle-Trip-and-Fuel-Log.git
```

### 2. Open the project folder

```bash
cd Rural-Transport-Vehicle-Trip-and-Fuel-Log/tripline
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Insert sample data

```bash
python sample_data.py
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

---

## Field Description

| Field | Meaning |
|---------|---------|
| record_id | Unique ID for each record |
| vehicle_no | Vehicle registration number |
| trip_date | Date of journey |
| start_km | Odometer reading before trip |
| end_km | Odometer reading after trip |
| distance | Total distance travelled (km) |
| fuel_litres | Fuel used during trip |
| driver | Driver name |
| efficiency | Distance travelled per litre of fuel |
| status | Vehicle performance category |

---

## Derived Value Calculation

The application automatically calculates:

```text
Distance = End KM − Start KM

Efficiency = Distance ÷ Fuel Litres
```

### Vehicle Status Rules

- Good → Efficiency ≥ 16 km/l
- Average → Efficiency between 12 and 15.99 km/l
- Poor → Efficiency < 12 km/l

These values are recalculated automatically whenever a record is added or updated.

---

## Dataset Information

The project contains 20+ sample trip and fuel records.

### Awkward Test Cases Included

- Repeated driver names
- An unusually old trip date (2018)
- Vehicles with poor fuel efficiency
- Multiple records for the same vehicle

These cases were included to test validation, filtering, and error handling.

---

## Testing Performed

✔ Added new trip records

✔ Updated existing records

✔ Verified automatic efficiency recalculation

✔ Tested search and filter functionality

✔ Verified records remain after page reload

✔ Tested empty state when no records exist

✔ Tested invalid input validation

✔ Verified calculated efficiency manually against dataset values

---

## Project Structure

```text
Rural-Transport-Vehicle-Trip-and-Fuel-Log/
│
├── tripline/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── requirements.txt
│   ├── database.db
│   ├── sample_data.py
│   ├── update_status.py
│   └── check_db.py
│
└── README.md
```

---

## Screenshots

### Home Page

<img width="1855" height="876" alt="image" src="https://github.com/user-attachments/assets/eb66dd3c-1512-4497-9306-e3772fb7f1bb" />

### Trip Entry Form

<img width="1830" height="876" alt="image" src="https://github.com/user-attachments/assets/133e21c6-731b-46e8-aa08-b17f5bad4844" />

### Trip Records

<img width="1782" height="876" alt="image" src="https://github.com/user-attachments/assets/efe852fe-960f-421b-b2b8-7540ff574974" />

### Filtering Records

<img width="1782" height="870" alt="image" src="https://github.com/user-attachments/assets/8a17c880-1122-4647-a1dd-95aea4da426c" />

---

## Current Limitations

- No user authentication
- No fuel cost analysis
- No vehicle maintenance tracking
- No report export functionality
- No GPS integration

---

## Author

**Shruthi T P**

GitHub: https://github.com/shruthi25307

---

## License

This project was developed for educational and learning purposes.
