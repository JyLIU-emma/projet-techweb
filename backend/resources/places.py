from flask import Flask, request, render_template
from flask_restful import Resource, Api

# from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']

geonames = {
    '2659815':{
        'geonameid':'2659086',
        'name': 'Lucelle',
        'asciiname': 'Lucelle',
        'latitude': '46.30352',
        'longitude': '6.82838'
    },
    '2659086':{
        'geonameid':'2659086',
        'name': 'Col de Recon',
        'asciiname': 'Col de Recon',
        'latitude': '47.41667',
        'longitude': '7.5'
    }
}

class AddPlace(Resource):
    def get(self):
        return "add form"
    def post(self):
        return "add a place in db"


##############################################
class SearchPlaces(Resource):
    def get(self):
        city = request.args['city']
        for item in geonames:
            print(item)
            if geonames[item]['name'] == city:
                city_info = geonames[item]
                break
        return {'the city in search':city, 'its info':city_info}
    
    def post(self):
        return "redirect to a specific place"

class PlaceInfoPage(Resource):
    def get(self):
        return "info of a certain place"
    def put(self):
        return "update the info"
    def delete(self):
        return "delete this place in db"