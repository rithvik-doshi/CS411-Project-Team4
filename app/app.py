from flask import Flask, render_template, request, send_from_directory
import re
from keys import keys
import requests

# API VARIABLES
flight_apiUrl = "https://aeroapi.flightaware.com/aeroapi/"
flight_apiKey = keys.flight_apiKey
weather_apiKey = keys.weather_apiKey


app = Flask(__name__, static_folder='client/build', static_url_path="/")


@app.route("/", methods=["GET"])
def hello():

    return app.send_static_file('index.html')



@app.route("/search", defaults={"flight_num": None}, methods=["GET"])
@app.route("/search/<string:flight_num>", methods=['GET'])
def search(flight_num=None):

    res = api_query(flight_num)

    return res.json()



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
