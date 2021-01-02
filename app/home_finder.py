from flask import Flask, render_template, request, url_for
from app.maps_logic import get_suitable_postcodes
from app.load_postcodes import load_postcodes
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postcodes/', methods=["POST"])
def postcodes():
    postcodes = load_postcodes()
    postcodes_list = get_suitable_postcodes(postcodes, request.form["office_postcode"], int(request.form["commute_time"]))
    return json.dumps(postcodes_list)

if __name__ == "__main__":
    app.run(debug=True)