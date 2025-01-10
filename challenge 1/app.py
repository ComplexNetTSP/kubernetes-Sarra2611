# app.py
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_url = request.url 
    return f"""
    <h1>Name: Sarra Barnoussi</h1>
    <h2>Project Name: My Flask Docker App</h2>
    <h3>Version: V1</h3>
    <h4>Server Hostname (Full URL): {current_url}</h4>
    <h5>Current Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</h5>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
