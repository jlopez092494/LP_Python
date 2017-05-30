from PIL import Image
import googlemaps
import json
import collections
from flask import Flask, jsonify, request

flThing = Flask(__name__)

@flThing.route('/ejercicio1', methods = ['POST'])
def getDirection():
    gmaps = googlemaps.Client(key='AIzaSyAAbZMe1pZtcETxTFcFIzXWykHRAY3xHOY')

    try:
        origin = request.json['origen']
        destination = request.json['destino']
    except:
        err={"Error": "Origen y/o Destino no escritos"}
        return jsonify(err), 400

    dir_res = gmaps.directions(origin, destination)
    direcciones = "{\n \"ruta\":[\n"

    for index in range(len(dir_res[0]['legs'][0]['steps'])):
        direcciones += "  {\n   \"lat\": "
        direcciones += str(dir_res[0]['legs'][0]['steps'][index]['start_location']['lat']) + ","
        direcciones += "\n   \"lon\": "
        direcciones += str(dir_res[0]['legs'][0]['steps'][index]['start_location']['lng'])
        
        if index == len(dir_res[0]['legs'][0]['steps']) - 1:
            direcciones += "\n  }\n"
        else:
            direcciones += "\n  },\n"
    
    direcciones += " ]\n}"
    print(direcciones)
    return direcciones, 401


@flThing.route('/ejercicio2', methods = ['POST'])
def getRestaurants():
    gmaps = googlemaps.Client(key='AIzaSyAAbZMe1pZtcETxTFcFIzXWykHRAY3xHOY')
    
    try:
        origin = request.json['origen']
    except:
        err={"Error":"Origen no escrito"}
        return jsonify(err), 400

    geo_res = gmaps.geocode(origin)
    resu = gmaps.places_nearby( ( geo_res[0]['geometry']['location']['lat'], geo_res[0]['geometry']['location']['lng'] ) , 30000, type = 'restaurant', keyword = 'restaurant')
    
    restaurantes = "{\n \"restaurantes\":[\n"

    for index in range(len(resu['results'])):
        restaurantes += "  {\n   \"nombre\": \""
        restaurantes += str(resu['results'][index]['name'])
        restaurantes += "\",\n"
        restaurantes += "   \"lat\": "
        restaurantes += str(resu['results'][index]['geometry']['location']['lat'])
        restaurantes += ",\n"
        restaurantes += "   \"lon\": "
        restaurantes += str(resu['results'][index]['geometry']['location']['lng'])
        
        if index == len(resu['results'])-1:
            restaurantes += "\n  }\n"
        else:
            restaurantes += "\n  },\n"
        
    restaurantes += " ]\n}"

    return restaurantes, 401


if __name__ == '__main__':
    flThing.run(port = 8686, debug = True)