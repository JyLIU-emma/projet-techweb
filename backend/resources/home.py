from flask import Flask, request, render_template
from flask_restful import Resource, Api

# from .lib.utils import *

__all__ =['Home']

class Home(Resource):
    def get(self):
        return "welcome page"   # welcome, choose connexion/creation du compte

    def post(self):
        return "redirect to login or create"  #redirect to different page