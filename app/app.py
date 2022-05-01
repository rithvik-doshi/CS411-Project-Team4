from flask import Flask, render_template, request, send_from_directory
import re
from keys import keys
import requests
from parse import parser

# API VARIABLES
flight_apiUrl = "https://aeroapi.flightaware.com/aeroapi/"
flight_apiKey = keys.flight_apiKey
weather_apiKey = keys.weather_apiKey


app = Flask(__name__, static_folder='client/build', static_url_path="/")


@app.route("/", methods=["GET"])
def hello():

    return app.send_static_file('index.html')


@app.route("/search", defaults={"flight_num": None}, methods=["GET"])
@app.route("/search/<string:flight_num>/<string:date>", methods=['GET'])
def search(flight_num=None, date=None):

    res = api_query(flight_num, date)

    return res.json()


def api_query(flight_number, date):

    print("new REAL api call!")

    ident = re.sub(r'[^a-zA-Z0-9]', '', flight_number).upper().replace(" ", "")
    # Create a regex to validate YYYY-MM-DD?
    payload = {'max_pages': 2}
    auth_header = {'x-apikey': flight_apiKey}

    response = requests.get(flight_apiUrl + f"flights/{ident}",
                            params=payload, headers=auth_header)

    if response.status_code == 200:
        # print(response.json())
        pass
    else:
        print("Error executing request")

    json_object = response._content

    response._content = parser(json_object, date)

    return response


if __name__ == "__main__":
    app.run(debug=True)
