from flask import Flask, render_template, request, redirect, session, jsonify, send_file
import sqlite3
import datetime
import random
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
app.secret_key = "secretkey"

# -----------------------
# DATABASE SETUP
# -----------------------

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature INTEGER,
        vibration TEXT,
        oil TEXT,
        battery TEXT,
        noise TEXT,
        result TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# -----------------------
# EXPERT SYSTEM
# -----------------------

def maintenance_expert_system(data):

    temperature = int(data["temperature"])
    vibration = data["vibration"]
    oil = data["oil"]
    battery = data["battery"]
    noise = data["noise"]

    suggestions = []

    if temperature > 85 and vibration == "High":
        suggestions.append("⚠ Bearing Wear Suspected")

    if oil == "Low":
        suggestions.append("🛢 Refill Lubrication Immediately")

    if battery == "Low":
        suggestions.append("🔋 Replace Battery")

    if vibration == "High" and noise == "High":
        suggestions.append("🔧 Shaft Misalignment Suspected")

    if temperature > 90:
        suggestions.append("🔥 Critical Overheating! Shut Down Motor")

    if not suggestions:
        suggestions.append("✅ Motor Operating Normally")

    return suggestions

# -----------------------
# LOGIN
# -----------------------

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")

        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")


# -----------------------
# DASHBOARD
# -----------------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.pop("user",None)
    return redirect("/")


# -----------------------
# CHECK MOTOR
# -----------------------

@app.route("/check", methods=["GET","POST"])
def check():

    if "user" not in session:
        return redirect("/")

    result=None

    if request.method == "POST":

        data=request.form
        result=maintenance_expert_system(data)

        conn=sqlite3.connect("database.db")
        c=conn.cursor()

        c.execute("""
        INSERT INTO logs(temperature,vibration,oil,battery,noise,result,timestamp)
        VALUES(?,?,?,?,?,?,?)
        """,(
            data["temperature"],
            data["vibration"],
            data["oil"],
            data["battery"],
            data["noise"],
            ", ".join(result),
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

    return render_template("index.html", result=result)


# -----------------------
# SENSOR SIMULATION API
# -----------------------

@app.route("/simulate")
def simulate():

    data={
        "temperature":random.randint(60,100),
        "vibration":random.choice(["Low","Medium","High"]),
        "oil":random.choice(["Normal","Low"]),
        "battery":random.choice(["Normal","Low"]),
        "noise":random.choice(["Low","High"])
    }

    return jsonify(data)


# -----------------------
# PDF REPORT
# -----------------------

@app.route("/download")
def download():

    conn=sqlite3.connect("database.db")
    c=conn.cursor()

    c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 1")
    record=c.fetchone()

    conn.close()

    if not record:
        return "No report available. Please analyze motor first."

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(buffer,pagesize=letter)

    styles=getSampleStyleSheet()

    elements=[]

    elements.append(Paragraph("Industrial Motor Maintenance Report",styles["Heading1"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"Temperature: {record[1]} °C",styles["Normal"]))
    elements.append(Paragraph(f"Vibration: {record[2]}",styles["Normal"]))
    elements.append(Paragraph(f"Oil Level: {record[3]}",styles["Normal"]))
    elements.append(Paragraph(f"Battery Status: {record[4]}",styles["Normal"]))
    elements.append(Paragraph(f"Noise Level: {record[5]}",styles["Normal"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph("Maintenance Suggestions:",styles["Heading2"]))
    elements.append(Paragraph(record[6],styles["Normal"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"Generated On: {record[7]}",styles["Normal"]))

    doc.build(elements)

    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="Motor_Report.pdf")


# -----------------------
# API ENDPOINT
# -----------------------

@app.route("/api/check",methods=["POST"])
def api():

    data=request.json

    result=maintenance_expert_system(data)

    return jsonify({"suggestions":result})


# -----------------------

if __name__=="__main__":
    app.run(debug=True)