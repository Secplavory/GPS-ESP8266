from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

lat = "";
long = "";
time = "";
date = "";

@app.route('/updateLocation', methods=['POST'])
def updateLocation():
    global lat, long, time, date

    content = request.json
    lat = content['lat']
    long = content['long']
    time = content['time']
    date = content['date']

    return jsonify({"status": "0000"})

@app.route('/getLocation', methods=['GET'])
def getLocation():
    global lat, long, time, date

    return jsonify(
        {
            "lat": lat,
            "long": long,
            "time": time,
            "date": date
        }
    )
