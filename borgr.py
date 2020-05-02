import socket, requests
import os
from radar import RadarClient
import re
from flask import Flask, request
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():

    ipU = request.environ['REMOTE_ADDR']

    # initialize client
    radar = RadarClient('prj_test_pk_d75f2dd9a1887939b58e7b9dcbf4c3c81e0f47d2')

    return request.headers['X-Forwarded-For']

    #geocode, ip = ipU
    cod = radar.geocode.ip()
    print(cod.latitude)
    print(cod.longitude)

    print("COD ",cod)

    user_location=(cod.latitude,cod.longitude)
    search = radar.search.places(near=user_location, categories="burger-restaurant")
    print(search[0].name)
    name = search[0].name
    addr = radar.search.autocomplete(name, near=user_location)
    print(addr[0].formattedAddress)

    toFormat = str(name)
    toFormat = toFormat.lower()
    toFormat = toFormat.replace(" ","+")
    print(toFormat)

    addr = "https://www.google.com/maps/search/"+toFormat+"/@"+str(cod.latitude)+","+str(cod.longitude)
    print(addr)

    #webbrowser.open_new_tab(addr)

    return addr

#https://www.google.com/maps/search/branded+burger+co/@32.5131302,-96.9722533

#67.180.133.255

if __name__ == "__main__":
    app.run(debug=True)
