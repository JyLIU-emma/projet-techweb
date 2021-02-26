from flask import Flask, request, flash, url_for, redirect, render_template, session
import json
import os
from flask_restful import Resource, Api

from .lib.utils import *


__all__ =['Login', 'CreateAdmin']

false = False
true = True

users = {
    "001": {
        "id": "001",
        "nom": "Mikolov",
        "prenom": "Thomas",
        "fonction": "Directeur des representations vectorielles",
        "anciennete": 10,
        "mise_a_jour": "2017-05-06 11:25:11.827000",
        "conge": 15,
        "actif": false,
        "actionnaire": true,
        "missions": ["Bruxelle", "Paris", "Pakistan"]
    },
    "002": {
        "id": "002",
        "nom": "Bergier",
        "prenom": "Francine",
        "fonction": "Chef service matériel informatique",
        "anciennete": 20,
        "mise_a_jour": "2011-01-05 06:20:31.527000",
        "conge": 14,
        "actif": true,
        "actionnaire": false,
        "missions": ["Paris"]
    }
    }

class Login(Resource):
    def get(self, userid):
        test1()
        return {userid:users[userid], 'nom': username, 'mot de passe': password}
    
    def post(self):
        """
        first:
        http://127.0.0.1:5000/admins/login/002?field=fonction

        {
            "002": "Chef service matériel informatique"
        }

        second:
        http://127.0.0.1:5000/admins/login
        postman: body form-data 输入信息
        """
        #first:
        # searchfield = request.args['field']  # searchfield 是我们想查询的字典里的键
        # return {userid:users[userid][searchfield]}


        #second：
        username = request.form.get('username')
        password = request.form.get('password')

        for user in users:
            if username == users[user]['nom']:
                msg = f"welcome, {username}"
                return {'message': msg, 'userinfo':users[user]}
            return "Hello stranger"



class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        return "redirect to gestionDb if success"