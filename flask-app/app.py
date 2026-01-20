from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# MongoDB connection (container service name from Docker Compose)
MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
MONGO_USER = os.environ.get("MONGO_USER", "myUser")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "myPassword")

client = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
)
db = client["test"]
collection = db["users"]

# --- /api route reading JSON from file ---
@app.route("/api")
def api():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Home route with form ---
@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if not name or not email:
            error = "Please fill all fields."
        else:
            try:
                collection.insert_one({"name": name, "email": email})
                return redirect(url_for("success"))
            except Exception as e:
                error = f"Error: {str(e)}"
    return render_template("form.html", error=error)

# --- Success page ---
@app.route("/success")
def success():
    return render_template("success.html")

# --- Run Flask app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

