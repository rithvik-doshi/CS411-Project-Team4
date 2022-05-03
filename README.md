# CS411-Project-Team4
CS411-Project-Team4 is working on a super cool project for class.

## Idea
Chances-of-flight-cancellation app, where we take the user’s selected flight, query it, find the weather forecast in the departing and arriving cities, and return some calculated probability that the flight will be canceled. The user can store their info in a DB and we can require users to make an account. Requires a flight-path and weather API (AeroAPI and OpenWeather API). An e-mail will be sent to those users whose flight has a high probability of being canceled based on our forecast.

## API Links

https://flightaware.com/commercial/aeroapi

https://openweathermap.org/price

## Dependencies

Python 3.7+
Flask
requests
flask-mongoengine