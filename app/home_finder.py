from flask import Flask, render_template, request, url_for
from maps_logic import get_suitable_postcodes
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/postcodes', methods=["POST"])
def postcodes():
    postcodes = ["IG12SZ", "N87EB"]  # Note this is a placeholder postcodes to check against
    postcodes_list = get_suitable_postcodes(postcodes, request.form["office_postcode"], int(request.form["commute_time"]))
    return json.dumps(postcodes_list)

if __name__ == "__main__":
    app.run(debug=True)