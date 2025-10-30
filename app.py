from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.data.gov.in/resource/ee03643a-ee4c-48c2-ac30-9f2ff26ab722?api-key=579b464db66ec23bdd0000013f631c0b762045036d516ffdf0484608&format=json&filters%5Bstate_name%5D=TELANGANA&filters%5Bfin_year%5D=2023-2024"

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
