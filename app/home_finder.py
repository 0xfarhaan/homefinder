from flask import Flask, render_template, request
from app.maps_logic import get_suitable_postcodes
from app.load_postcodes import load_postcodes

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/postcodes/", methods=["POST"])
def postcodes() -> dict:
    """returns postcode districts that are within the commute time to the office via public transport"""
    postcodes_dict = get_suitable_postcodes(
        load_postcodes(),
        request.form["office_postcode"],
        int(request.form["commute_time"]),
    )
    return postcodes_dict