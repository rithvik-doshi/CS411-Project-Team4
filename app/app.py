from flask import Flask, render_template, request, send_from_directory
import re
from keys import keys
import requests

# API VARIABLES
flight_apiUrl = "https://aeroapi.flightaware.com/aeroapi/"
flight_apiKey = keys.flight_apiKey
weather_apiKey = keys.weather_apiKey


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():

    res = api_query("AS136")

    return res.json()


@app.route("/search", methods=["POST"])
def search():

    username = request.form["username"]
    # sanitize the username to only alphanumerics
    username = re.sub(r'\W+', '', username)

    res = api_query(username)

    return "res"


def api_query(flight_number):

    print("new REAL api call!")

    ident = flight_number
    payload = {'max_pages': 2}
    auth_header = {'x-apikey':flight_apiKey}

    response = requests.get(flight_apiUrl + f"flights/{ident}",
        params=payload, headers=auth_header)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error executing request")

    return response


if __name__ == "__main__":
    app.run(debug=True)
