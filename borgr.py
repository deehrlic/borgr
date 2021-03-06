import socket, requests
import os
from radar import RadarClient
import re
from flask import Flask, request, redirect, render_template
import webbrowser

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("frontpage.html")

@app.route('/handle', methods=['GET', 'POST'])
def home():

    ipU = request.environ['REMOTE_ADDR']

    # initialize client
    radar = RadarClient('prj_test_pk_d75f2dd9a1887939b58e7b9dcbf4c3c81e0f47d2')



    #geocode, ip = ipU
    cod = radar.geocode.ip(request.headers['X-Forwarded-For'])
    #cod = radar.geocode.ip('107.77.199.117')
    print(cod.latitude)
    print(cod.longitude)

    print("COD ",cod)

    user_location=(cod.latitude,cod.longitude)
    search = radar.search.places(near=user_location, categories="burger-restaurant")

    if len(search) == 0:
        return 'Radar.io does not think there is a burger restaurant near you. Try going on data and hitting the button again if you are on mobile. :('

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

    return redirect(addr)

#https://www.google.com/maps/search/branded+burger+co/@32.5131302,-96.9722533



if __name__ == "__main__":
    app.run(debug=True)
