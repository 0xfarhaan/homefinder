import csv
import os


def load_postcodes():
    """Loads all postcode districts for the London area from csv"""
    csv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../postcodes.csv')
    postcodes = []
    with open(csv_path, newline='') as inputfile:
        for row in csv.reader(inputfile):
            postcodes.append(row[0] + " London")

    return postcodes