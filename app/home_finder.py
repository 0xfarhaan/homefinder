from flask import Flask, render_template, request, url_for
from maps_logic import get_time_to_destination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/traveltime', methods=["POST"])
def traveltime():
    time = get_time_to_destination(request.form["start"], request.form["end"])
    return str(time)

if __name__ == "__main__":
    app.run(debug=True)