# 🚛 Rural Transport Vehicle Trip & Fuel Log

🌐 **Live Demo:** https://rural-transport-vehicle-trip-and-fuel-log.onrender.com/

A Flask-based web application designed to simplify vehicle trip management and fuel usage tracking for rural transportation services. The system enables transport operators to record trip details, monitor fuel consumption, and maintain organized travel logs for better operational efficiency.

---

## 📌 Features

- Record vehicle trip details
- Maintain driver and vehicle information
- Track fuel consumption for each trip
- Calculate trip distance and fuel usage
- View complete trip history
- Update trip status
- Responsive and user-friendly interface
- SQLite database for lightweight data storage

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Python
- Flask

### Database
- SQLite

### Deployment
- Render

---

## 📂 Project Structure

```
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

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/shruthi25307/Rural-Transport-Vehicle-Trip-and-Fuel-Log.git
```

### Navigate to the project folder

```bash
cd Rural-Transport-Vehicle-Trip-and-Fuel-Log/tripline
```

### Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The application will be available at

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

The application is deployed on Render.

**Live Website**

https://rural-transport-vehicle-trip-and-fuel-log.onrender.com/

---

## 📋 Application Workflow

1. Enter trip details.
2. Select vehicle and driver information.
3. Record fuel consumed during the journey.
4. Save trip information.
5. View all recorded trips.
6. Update trip status whenever required.

---

## 📸 Screenshots

- Home Page
  <img width="1855" height="876" alt="image" src="https://github.com/user-attachments/assets/eb66dd3c-1512-4497-9306-e3772fb7f1bb" />
  
- Trip Entry Form
  <img width="1830" height="876" alt="image" src="https://github.com/user-attachments/assets/133e21c6-731b-46e8-aa08-b17f5bad4844" />
  
- Trip Records
  <img width="1782" height="876" alt="image" src="https://github.com/user-attachments/assets/efe852fe-960f-421b-b2b8-7540ff574974" />
  
- Filtering Records
  <img width="1782" height="870" alt="image" src="https://github.com/user-attachments/assets/8a17c880-1122-4647-a1dd-95aea4da426c" />

---

## Future Enhancements

- User Authentication
- Vehicle Maintenance Tracking
- Fuel Cost Analytics
- GPS Integration
- Route Optimization
- Export Reports (PDF/Excel)
- Dashboard with Charts
- Multi-user Support

---

## 👩‍💻 Author

**Shruthi T P**

GitHub: https://github.com/shruthi25307

---

## 📄 License

This project is developed for educational and learning purposes.
