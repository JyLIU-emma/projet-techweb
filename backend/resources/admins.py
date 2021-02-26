from flask import Flask, request, render_template
from flask_restful import Resource, Api

from .lib.utils import *


__all__ =['Login', 'CreateAdmin']

class Login(Resource):
    def get(self):
        test1()
        return "login page info"

class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        return "redirect to gestionDb if success"