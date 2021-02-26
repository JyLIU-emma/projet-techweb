from flask import Flask, request, render_template
from flask_restful import Resource, Api

# from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']

class AddPlace(Resource):
    def get(self):
        return "add form"
    def post(self):
        return "add a place in db"

class SearchPlaces(Resource):
    def get(self):
        return "result of search the querykey"
    
    def post(self):
        return "redirect to a specific place"

class PlaceInfoPage(Resource):
    def get(self):
        return "info of a certain place"
    def put(self):
        return "update the info"
    def delete(self):
        return "delete this place in db"