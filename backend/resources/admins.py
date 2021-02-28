from flask import Flask, request, flash, url_for, redirect, render_template, session, flash, jsonify
import json
import os
from flask_restful import Resource, Api

from .lib.utils import *


__all__ =['Login', 'CreateAdmin']

false = False
true = True

users = load_data('users')
admins = load_data('admins')

class Login(Resource):
    def get(self, userid):
        return jsonify({userid:users[userid], 'nom': username, 'mot de passe': password})
    
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

        session['name'] = username
        session['password'] = password

        # print(session['name'])
        # print(session['password'])

        if not all([username, password]):
            msg = "Rempliez tous les champs, s'il vous plaît!"
            return {'message' : msg}
        else:
            for user in users:
                if username == users[user]['nom'] and password == users[user]['id']:
                    msg = f"welcome, {username}"
                    return jsonify({'message': msg, 'userinfo':users[user]})
                elif username == users[user]['nom'] and password != users[user]['id']:
                    msg = "Le mot de passe n'est pas correct"
                    return jsonify({'message': msg})
            return jsonify({'message' : "Hello stranger"})



class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')
        password2 = request.form.get('passwordconfirm')

        if userid not in users.keys():
            msg = "Désolée, vous n'êtes pas notre collaborateur, vous ne pouvez pas créer un compte."
        elif userid in admins.keys():
            msg = "Vous avez déjà un compte."
        elif not all([username, userid, password, password2]):
            msg = "Veuillez remplir tous les champs."
        elif username != users[userid]["nom"] :
            msg = "Votre id ne conforme pas à votre nom. "
        elif password != password2 :
            msg = "Les deux mots de passe remplis doivent être identiques."
        else:
            admins[userid] = {
                    'id': userid,
                    'nom': username,
                    'mot de passe': password
                    }
            msg = "Votre compte admin a bien été créé."
        
        # print(admins)
        dict_to_json(admins, "admins")

        return jsonify({"massage" : msg})