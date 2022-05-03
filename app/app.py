from flask import Flask, render_template, request, send_from_directory
import re
from keys import keys
import requests
import json

from flask_mongoengine import MongoEngine

from parse import parser
# from templates import *

# API VARIABLES
flight_apiUrl = "https://aeroapi.flightaware.com/aeroapi/"
flight_apiKey = keys.flight_apiKey
weather_apiKey = keys.weather_apiKey


app = Flask(__name__, static_folder='client/build', static_url_path="/")


# Database configuration

app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
    "host": "localhost",
    "port": 27017,
}
db = MongoEngine(app)



class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)

class Flight(db.Document):
    owner = db.StringField(required=True)       # username of owner
    flight_num = db.StringField(required=True)
    flight_date = db.StringField(required=True) # YYYY-MM-DD



# Deliver the react.js frontend
@app.route("/", methods=["GET"])
def hello():

    return app.send_static_file('index.html')


# // // REPLACE THIS WITH ACTUAL OATH // //

# Add a new user to the database
@app.route("/add_user/<string:username>/<string:password>")
def add_user(username=None, password=None):     # test/testpass

    # Create new object to save
    new_user = User(username=username, password=password)

    # Check if this user already exists
    if User.objects(username=username).first() != None:
        return '{status: "error", error: "user already exists!"}'

    # Add the user to the database
    new_user.save()

    return '{status: "ok"}'


# Check if a username and password match
@app.route("/check_user/<string:username>/<string:password>")
def check_user(username=None, password=None):

    # Check if user with this username and password exists
    if User.objects(username=username, password=password).first() == None:
        return '{status: "error", error: "username and/or password is invalid"}'

    # If user is found return success and the valid username
    return '{status: "ok", username: "' + username + '"}'


# // // End Horribly insecure code // //



# Add a new tracked flight to database
@app.route("/add_flight/<string:flight_num>/<string:date>/<string:username>", methods=["GET"])
def add_flight(flight_num=None, date=None, username=None):

    # Create new object to save
    new_flight = Flight(owner=username, flight_num=flight_num, flight_date=date)

    # Check if user is valid
    if User.objects(username=username).first() == None:
        return '{status: "error", error: "username not valid"}'

    # Add flight to database
    new_flight.save()

    return '{status: "ok"}'



# Return all of a user's tracked flights (and query the apis for most up to date data)
@app.route("/get_flights/<string:username>", methods=["GET"])
def get_flights(username=None):

    # Check if user is valid
    if User.objects(username=username).first() == None:
        return '{status: "error", error: "username not valid"}'

    # Get all flights belonging to that user
    flights = Flight.objects(owner=username)

    flight_dict = {}

    if flights.first() == None:
        return "empty"

    for x in flights:
        flight_dict[x] = "poggers"
        # flight_dict[x.id] = {

        # }1222

    return json.dumps(flight_dict)





@app.route("/search", defaults={"flight_num": None}, methods=["GET"])
@app.route("/search/<string:flight_num>/<string:date>", methods=['GET'])
def search(flight_num=None, date=None):

    res = api_query(flight_num, date)

    return res.json()


def api_query(flight_number, date):

    print("new flight api call")

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
