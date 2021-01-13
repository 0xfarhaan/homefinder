import googlemaps
import os
from datetime import datetime

API_KEY = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=API_KEY)


def format_time_to_mins(time: int) -> int:
    """formats time from seconds to the nearest minute"""
    return int(round(time / 60))


def get_time_to_destination(start: str, end: str) -> int:
    """returns the transit time between two destinations using google maps api"""
    now = datetime.now()
    directions_result = gmaps.directions(start, end, mode="transit", departure_time=now)

    return format_time_to_mins(directions_result[0]["legs"][0]["duration"]["value"])


def get_suitable_postcodes(postcodes_to_check: list, office_postcode: str, commute_time: int) -> dict:
    """checks commute time from office and returns postcodes that are in the desired commute time."""
    suitable_postcodes = {"Postcodes": []}
    for postcode in postcodes_to_check:
        if get_time_to_destination(postcode, office_postcode) <= commute_time:
            suitable_postcodes["Postcodes"].append(postcode.split(" ")[0])

    return suitable_postcodes
