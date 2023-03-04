from flask import Flask,render_template, request, jsonify
from date import date
from geopy.geocoders import Nominatim
import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from timezonefinder import TimezoneFinder
from datetime import datetime
from flask import jsonify, Flask, request
import pytz


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/<nr>/apply")
def search(nr):
    data = request.args
    nr=data['phone_number']
    informatii = date(nr,geocoder)
    return render_template('info.html', dict_info=informatii)

if __name__ == "__main__":
    app.run(debug=True)