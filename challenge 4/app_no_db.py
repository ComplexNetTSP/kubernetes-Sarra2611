from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Flask App Without DB</h1>
    <h3>Version: V1</h3>
    <h5>Current Date: {current_date}</h5>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
