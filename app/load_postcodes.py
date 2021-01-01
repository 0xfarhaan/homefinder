import csv
import os


def load_postcodes():
    csv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../postcodes.csv')
    postcodes = []  # postcodes for harringay
    with open(csv_path, newline='') as inputfile:
        for row in csv.reader(inputfile):
            postcodes.append(row[0])

    return postcodes