from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template('index.html')   # welcome, choose connexion/creation du compte

    def post(self):
        return "upload login infomation"  #redirect to different page