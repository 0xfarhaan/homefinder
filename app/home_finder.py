from flask import Flask, render_template, request, url_for
from maps_logic import get_time_to_destination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/traveltime', methods=["POST"])
def traveltime():
    data = request.form
    time = get_time_to_destination(data["start"], data["end"])
    return time

if __name__ == "__main__":
    app.run(debug=True)