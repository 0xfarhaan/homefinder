# Home Finder

## About:
Home Finder is a web app that allows a person who is looking to move into North/North-West London
search for postcode districts that fall within the desired commute time to their office.

## How to use:
Please find a deployed version [here](https://tranquil-sea-13127.herokuapp.com/)

Once on the website fill the form with the postcode of your office and desired commute time in minutes.
You will then be returned postcode districts that fulfil your criteria. 

## Running locally:
It is possible to run the app locally, but you will need to have your own googlemaps api key.

1. Clone this repository and navigate to its directory.
2. Setup your virtual environment, activate it then install the requirements as described below
```bash
$ python -m  venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
3. Set your googlemaps api key using the enviroment variable API_KEY.
```bash
$ export API_KEY="insert api key here"
```
4. Set your flask app variable.
```bash
$ export FLASK_APP=app.home_finder.py
```
5. Run app using the following command.
```bash
$ flask run
```

## Running Tests:
First you must follow the running locally instructions. Then whilst in the root of the project
run the following command.
```bash
$ pytest -rA .
```

## Technologies:

| Area                 | Technology                 |
| -------------------- | -------------------------- |
| Language           | Python, HTML, CSS|
| Frameworks         | Flask, Bootstrap|
| Testing            | Pytest|
|Other              | Google Maps

## Future Developments:
For more information refer to the github project board.

- Add the ability to check multiple office locations.
- Add map highlighting on postcode districts as response.


