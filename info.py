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

def search(geocoder=geocoder):
    global lat
    global lng
    global location
    global map_count
    global current_time
    global time_zone_ans

    map_count = 0
    data = request.args
    enter_number=data['phone_number']
    pepnumber=phonenumbers.parse(enter_number)

    location_1 = geocoder.description_for_number(pepnumber,'en')

    # carier
    service_pro = phonenumbers.parse(enter_number)
    if carrier.name_for_number(service_pro,'en') == '':
        phone_carrier_ans='Just for mobile phone'
    else:
        phone_carrier_ans=carrier.name_for_number(service_pro,'en')
    # Time Zone
    number=phonenumbers.parse(enter_number)
    time=timezone.time_zones_for_number(number)
    time_zone=time

    key = '05f849c9bc0141d8ac2465fdfe7c39de'
    geocoder = OpenCageGeocode(key)
    query = str(location_1)
    result = geocoder.geocode(query)
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    gps_button=f'{lat}, {lng}'
    country_s = result[0]['components']['country']
    country_ans=country_s
    continent = result[0]['components']['continent']
    continent_ans=continent
    try:
        country_code = result[0]['components']['ISO_3166-1_alpha-2']
        country_code_ans=country_code
    except:
        pass
    currency = result[0]['annotations']['currency']['iso_code']
    symbol = result[0]['annotations']['currency']['symbol']
    currency_ansf='{currency},  {symbol}'
    currency_name = result[0]['annotations']['currency']['name']
    currency_name_ans=currency_name
    # wikidata = result[0]['annotations']['wikidata']

    #time showing in phone
    geolocator = Nominatim(user_agent='geoapiEx')
    location= geolocator.geocode(location_1,language='en')
    location_ans=location
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%I:%M.%p')
    time_zone_ans=current_time
