from flask import Flask, request, url_for, redirect, session, flash, jsonify, abort
import json
# from flask_login import LoginManager, UserMixin, login_required, logout_user
from flask_login import login_user, logout_user, login_required
import os
from flask_restful import Resource, Api
from passlib.apps import custom_app_context as pwd_context
import jwt
from .lib.utils import *


__all__ =['Login', 'CreateAdmin', 'Logout']

false = False
true = True


users = load_data('users')
#admins = load_data('admins')



class Login(Resource):
    def get(self, userid):
        return jsonify({userid:users[userid], 'nom': username, 'mot de passe': password})
    
    def post(self):
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')

        if not all([username, password, userid]):
            msg = "Remplissez tous les champs, s'il vous plaît!"
            abort(400, msg)

        #session['name'] = username
        #session['id'] = userid
        #session['password'] = password

        user = User.query.filter_by(id = userid).first()
        if not user or not user.verify_password(password):
            msg = "Vérifiez votre nom, votre id ou votre mot de passe, s'il vous plaît !"
            abort(400, msg)
        #----增加----#
        else:
            login_user(user, remember = False)
            return jsonify({"message" : "Bienvenu."})


class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return jsonify({'message':"Vous êtes sorti le système."})


class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        username = request.form.get('username')
        #print(username)
        userid = request.form.get('id')
        #print(userid)
        password = request.form.get('password')
        password2 = request.form.get('passwordconfirm')

        if not all([username, userid, password, password2]):
            abort(400, "Veuillez remplir tous les champs.") #missing arguments
        elif userid not in users.keys():
            abort(400, "Désolée, vous n'êtes pas notre collaborateur, vous ne pouvez pas créer un compte.")
        elif User.query.filter_by(username = username).first() is not None:
            abort(400, 'Vous avez déjà un compte.') #existing user
        elif username != users[userid]["nom"] :
            abort(400, "Votre id ne conforme pas à votre nom. ")
        elif password != password2 :
            abort(400, "Les deux mots de passe remplis doivent être identiques.")

        user = User(username = username, id = userid)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        msg = "Votre compte admin a bien été créé."
        
        # print(admins)
        # dict_to_json(admins, "admins")

        return jsonify({"massage" : msg})
