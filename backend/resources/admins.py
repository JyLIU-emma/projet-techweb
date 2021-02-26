from flask import Flask, request, flash, url_for, redirect, render_template, session, flash
import json
import os
from flask_restful import Resource, Api

from .lib.utils import *


__all__ =['Login', 'CreateAdmin']

false = False
true = True

users = load_data('users')

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

        session['name'] = username
        session['password'] = password

        print(session['name'])
        print(session['password'])

        if not all([username, password]):
            msg = "Rempliez tous les champs, s'il vous plaît!"
            return {'message' : msg}
        else:
            for user in users:
                if username == users[user]['nom'] and password == users[user]['id']:
                    msg = f"welcome, {username}"
                    return {'message': msg, 'userinfo':users[user]}
                elif username == users[user]['nom'] and password != users[user]['id']:
                    msg = f"Le mot de passe n'est pas correct"
                    return {'message': msg}
            return "Hello stranger"



class CreateAdmin(Resource):
    def get(self):
        return "formulaire d'inscrire admin template"
    
    def post(self):
        return "redirect to gestionDb if success"