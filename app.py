from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return render_template('index.html')   # welcome, choose connexion/creation du compte

    def post(self):
        return "upload login infomation"  #redirect to different page

class Login(Resource):
    def get(self):
        return "login page template"

class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        return "redirect to gestionDb if success"

class GestionDb(Resource):
    def get(self):
        return "choose between search/add"

class Search(Resource):
    def get(self):
        return "result of search"

class PlaceInfoPage(Resource):
    def get(self):
        return "info of a certain place"
    def put(self):
        return "update the info"
    def delete(self):
        return "delete this place in db"

class AddPlace(Resource):
    def get(self):
        return "afficher le formulaire pour ajouter"
    def post(self):
        return "add the place in db"



api.add_resource(Home, '/', '/home')
api.add_resource(Login, '/login')  #se connecter
api.add_resource(CreateAdmin, '/admins/create')  #s'inscrire
api.add_resource(GestionDb, '/geonames/') # choose search/add
api.add_resource(Search, '/geonames/search')
####################################################
api.add_resource(PlaceInfoPage, '/geonames/<geonameid>')  # info de chaque endroit + delete + change
api.add_resource(AddPlace, '/geonames/add')  #page of add a place



if __name__ == '__main__':
    app.run(debug=True)

    