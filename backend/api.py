from flask import Flask, request, render_template, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

from pathlib import Path

from resources import *

app = Flask(__name__)
app.secret_key = '23rfqs'   ################# random string

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(DB_DATA)
app.config['SECRET_KEY'] = "random_string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

db.init_app(app)
api = Api(app)


api.add_resource(Home, '/', '/home')
api.add_resource(Login, '/admins/login', '/admins/login/<userid>')  #se connecter GET POST
api.add_resource(CreateAdmin, '/admins/create')  #s'inscrire GET POST
# api.add_resource(CreateAdmin, '/admins/<userid>') # GET choose search/add 
# api.add_resource(GestionDb, '/geonames/') # GET choose search/add   POST 
api.add_resource(AddPlace, '/geonames/add') #GET     POST add info
api.add_resource(SearchPlaces, '/geonames') 
# api.add_resource(SearchPlaces, '/geonames/<querykey>')   #  GET all the results find by querykey      POST geonameid ==> /geonames/<geonameid>
####################################################
api.add_resource(PlaceInfoPage, '/geonames/<geonameid>')  # info de chaque endroit + /geonames/<geonameid>/delete + /geonames/<geonameid>/change(PUT)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(port=2021, host='0.0.0.0')

    