import googlemaps
import os
from datetime import datetime
import csv

API_KEY = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=API_KEY)

csv_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../postcodes.csv')

postcodes = []  # postcodes for harringay
with open(csv_filename, newline='') as inputfile:
    for row in csv.reader(inputfile):
        postcodes.append(row[0])

def get_time_to_destination(start, end):
    """returns the transit time between two destinations using google maps api"""
    now = datetime.now()
    directions_result = gmaps.directions(start,
                                         end,
                                         mode="transit",
                                         departure_time=now)

    travel_time = directions_result[0]["legs"][0]["duration"]["text"]

    return travel_time