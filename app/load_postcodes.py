import csv
import os


def load_postcodes() -> list:
    """Loads all postcode districts for the London area from csv"""
    csv_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../postcodes.csv"
    )
    postcodes = []
    with open(csv_path, newline="") as inputfile:
        for row in csv.reader(inputfile):
            if "N" in row[0][0]:  # North / North-West London Only
                postcodes.append(row[0] + " London")

    return postcodes
