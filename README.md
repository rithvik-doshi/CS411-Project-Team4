# CS411-Project-Team4

CS411-Project-Team4 is working on a super cool project for class.

## Video Presentation:

https://drive.google.com/file/d/14TWPJ0gkf0j-z5-0dN1SJqxi8y1AmUid/view?usp=sharing

## Idea

Chances-of-flight-cancellation app, where we take the user’s selected flight, query it, find the weather forecast in the departing and arriving cities, and return some calculated probability that the flight will be canceled. The user can store their info in a DB and we can require users to make an account. Requires a flight-path and weather API (AeroAPI and OpenWeather API). An e-mail will be sent to those users whose flight has a high probability of being canceled based on our forecast.

## API Links

https://flightaware.com/commercial/aeroapi

https://openweathermap.org/price

## Dependencies

Python 3.7+
PyAirports (https://github.com/NICTA/pyairports)
Flask
requests
flask-mongoengine

## Installation and Setup

Install all python dependencies above with pip/pip3. Install and start mongod with the start.sh script in the /db folder under /app. Start the app with python3 app.py. navigate to 127.0.0.
