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
        return {userid:users[userid]}

class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        return "redirect to gestionDb if success"