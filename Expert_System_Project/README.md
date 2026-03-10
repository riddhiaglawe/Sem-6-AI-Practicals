# ⚙ AI-Based Expert System for Industrial Motor Maintenance
### Industrial Equipment Monitoring & Maintenance Advisory System

A web-based Expert System designed to assist in diagnosing and preventing failures in industrial motors.  
The system analyzes machine conditions such as temperature, vibration, oil level, battery status, and noise levels, and provides maintenance recommendations using a rule-based inference engine.

This project demonstrates how Artificial Intelligence techniques such as Expert Systems and Rule-Based Reasoning can be applied in industrial maintenance systems.

---

## 🚀 Features

- 🔧 Industrial Motor Condition Monitoring
- 🌡 Temperature Analysis
- 📊 Vibration Level Monitoring
- 🛢 Oil Level Detection
- 🔋 Battery Status Monitoring
- 🔊 Noise Level Detection
- 🧠 Rule-Based Expert System (AI)
- 📄 Maintenance PDF Report Generation
- 🗄 Maintenance Log Storage in Database
- 🔐 Login Authentication System
- 🌐 REST API for System Integration
- 📡 Simulated Sensor Data

---

## 🧠 How It Works

The system collects motor condition inputs such as:

- Temperature
- Vibration Level
- Oil Level
- Battery Status
- Noise Level

These inputs are processed using an expert system based on **IF–THEN rules**.

Example rule:

IF temperature > 85 AND vibration = High  
THEN Bearing Wear Suspected

The inference engine evaluates the conditions and generates maintenance suggestions to help technicians detect potential motor failures early.

---

## ⚙ Expert System Logic

The system uses a rule-based knowledge base.

Example rules:

- IF oil level = Low → Refill lubrication immediately
- IF vibration = High AND noise = High → Shaft misalignment suspected
- IF temperature > 90 → Critical overheating alert

These rules simulate the knowledge used by maintenance engineers in industrial environments.

---

## 📄 Maintenance Report Generation

The system generates a downloadable PDF report containing:

- Motor condition data
- Maintenance suggestions
- Timestamp of analysis

This helps maintain maintenance records and documentation.

---

## 📡 Sensor Data Simulation

Since real industrial sensors are not connected, the system simulates sensor readings such as:

- Temperature values
- Vibration levels
- Oil levels
- Noise levels

This mimics real industrial monitoring systems.

---

## 🛠 Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS
- Database: SQLite
- PDF Engine: ReportLab
- Version Control: Git & GitHub

---

## 📂 Project Structure

Expert_System_Project/
│
├── app.py                # Main Flask backend application
├── database.db           # SQLite database for maintenance logs
│
├── templates/
│   ├── login.html        # Login page
│   ├── dashboard.html    # Dashboard interface
│   └── index.html        # Motor condition check page
│
├── static/
│   └── style.css         # CSS styling
│
├── README.md             # Project documentation
