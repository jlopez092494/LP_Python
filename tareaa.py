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



if __name__ == '__main__':
    flThing.run(port = 8686, debug = True)