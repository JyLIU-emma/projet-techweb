from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import json
from passlib.apps import custom_app_context as pwd_context
#----增加----#
from flask_login import UserMixin
from flask_restful import Resource, Api
import jwt

__all__ = ["load_data", "dict_to_json", 'fr', 'db', 'DB_DATA']

# Créer des chemins vers les bases de données
BACKEND = Path(__file__).parent.parent.parent
DATA = BACKEND / "data"
USERS_DATA = DATA / "users.json"
ADMINS_DATA = DATA / "admins.json"
DB_DATA = DATA / "locations.db"

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token, app):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        # except SignatureExpired:
        #     return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user
    
def load_data(tablename):
    if tablename == "users":
        with USERS_DATA.open() as f:
            data_dico = json.load(f)
    elif tablename == "admins":
        with ADMINS_DATA.open() as f:
            try:
                data_dico = json.load(f)
            except Exception:
                data_dico = {}
    return data_dico

'''
def dict_to_json(dico, filename):
    json_str = json.dumps(dico, indent=4)
    if filename == "admins":
        filepath = ADMINS_DATA
    else:
        filepath = DATA / f"{filename}.json"

    with filepath.open(mode="w") as jsonfile:
        jsonfile.write(json_str)
'''


class fr(db.Model):
    geonameid = db.Column('geonameid', db.Integer, primary_key = True)
    name = db.Column(db.String)
    asciiname = db.Column(db.String)
    alternatenames = db.Column(db.String) 
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    feature_class = db.Column(db.String)
    feature_code = db.Column(db.String)
    country_code = db.Column(db.String)
    cc2 = db.Column(db.String)
    admin1_code = db.Column(db.Integer)
    admin2_code = db.Column(db.Integer)
    admin3_code = db.Column(db.Integer)
    admin4_code = db.Column(db.Integer)
    population = db.Column(db.Integer)
    elevation = db.Column(db.String)
    dem = db.Column(db.String)
    timezone = db.Column(db.String)
    modification_date = db.Column(db.String)

    def __init__(self, geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code, population, elevation, dem,
    timezone, modification_date):
        self.geonameid = geonameid
        self.name = name
        self.asciiname = asciiname
        self.alternatenames = alternatenames
        self.latitude = latitude
        self.longitude = longitude
        self.feature_class = feature_class
        self.feature_code = feature_code
        self.country_code = country_code
        self.cc2 = cc2
        self.admin1_code = admin1_code
        self.admin2_code = admin2_code
        self.admin3_code = admin3_code
        self.admin4_code = admin4_code
        self.population = population
        self.elevation = elevation
        self.dem = dem
        self.timezone = timezone
        self.modification_date = modification_date

def main():
    filepath = DATA / f"admins.json"
    with filepath.open() as f:
        data_dico = json.load(f)
    data_dico['006'] = {
                    'id': '006',
                    'nom': 'test',
                    'mot de passe': 'test'
                    } 
    dict_to_json(data_dico, 'try')

if __name__ == "__main__":
    main()
