# app.py
from flask import Flask, request
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client["flaskdb"]
logs = db["logs"]

@app.route("/")
def home():
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs.insert_one({"ip": client_ip, "date": current_date})

    # Fetch the last 10 records
    recent_logs = logs.find().sort("_id", -1).limit(10)
    log_display = "<br>".join([f"IP: {log['ip']}, Date: {log['date']}" for log in recent_logs])
    
    
    return f"""
    <h1>Name: Sarra Barnoussi</h1>
    <h2>Project Name: My Flask Docker App</h2>
    <h3>Version: V1</h3>
    <h4>Current Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</h4>
    <h5>Last 10 Logs:</h5>
    <p>{log_display}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
