from flask import Flask,render_template, request, jsonify
from date import date
from phonenumbers import geocoder
from flask import jsonify, Flask, request
import folium
import socket


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/<nr>/apply")
def search(nr):
    global info
    global numar

    data = request.args
    nr=data['phone_number']
    numar = data['phone_number']
    info = date(nr,geocoder)
    locatie = info['location'][0]
    lat = info['lat']
    lng = info['lng']
    return harta()
    # return render_template('info.html', info=info,nr=nr, map=map)

# @app.route('/map')
def harta():
    # myip = request.environ['REMOTE_ADDR']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        myip = request.environ['REMOTE_ADDR']
    else:
        myip= request.environ.get('HTTP_X_FORWARDED_FOR')

    locatie = info['location'][0]
    lat = info['lat']
    lng = info['lng']
    # f"<a href=https://phone-locator.onrender.com/>Search Again</a>"
    map = folium.Map(location=[lat,lng],width="60%",height="60%",  tiles= 'Stamen Terrain', zoom_start=6)
    folium.Marker(location=[lat,lng], tooltip=f"Your phone is located in {locatie}!",
                  popup=f"<a href=https://phone-locator.onrender.com/>Search Again</a>", icon=folium.Icon(color='red') ).add_to(map)
    map.get_root().html.add_child(folium.Element(f"""
        <html>
            <head>
                <title>Phone Tracker</title>
                <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
          rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
          crossorigin="anonymous">
            </head>
            <body>  
                <nav class="navbar bg-body-tertiary">
                  <div class="containner ">
                    <a class="navbar-brand" href="https://phone-locator.onrender.com/">
                    <img src="/static/icon.ico" alt="Phone Tracker" width="50" height="50">
                    <h1 class="text-left">New Search</h1></a>
                    
                  </div>
                  <h1 class="text-center mt-2 mb-4" >Phone Tracker</h1>
                </nav>          
                <div>
                    <h2 >
                        <p class="px-5">The number {numar} is registered in {info['location']} / {info['continent']}<br>
                    The country code is {info['country_code']}<br> The local currency is {info['currency']}, the symbol is {info['symbol']}<br>
                        Local time in {info['country']} is {info['current_time']}<br>{myip}
                        </p>
                    </h2>       
                </div>
            </body>
        </html>    
    """))
    return map._repr_html_()



if __name__ == "__main__":
    app.run(debug=True)