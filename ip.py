from flask import request
import requests

def ip():
    # myip = request.environ['REMOTE_ADDR']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        myip = request.environ['REMOTE_ADDR']
    else:
        myip = request.environ.get('HTTP_X_FORWARDED_FOR')

    # url = geo.ipinfo(myip)
    # info_ip=url[0]
    url = '5.14.129.88'
    info_ip = requests.get(f"https://geolocation-db.com/json/{url}&position=true").json()
    return info_ip