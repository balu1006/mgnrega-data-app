from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "API-KEY HERE"

@app.route("/", methods=["GET"])
def index():
    records = []
    error = None
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])
            print("Fetched records:", records)  # for debugging
            if not records:
                error = "No data returned for 'TELANGANA' and '2023-2024'."
        else:
            error = f"Could not fetch API data. Status code: {response.status_code}"
    except Exception as e:
        error = f"Error: {str(e)}"
    return render_template("index.html", records=records, error=error)

if __name__ == "__main__":
    app.run(debug=True)
