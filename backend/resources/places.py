from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']


# lister tous les infos à recueillir
info_list = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', \
            'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 'dem', 'timezone', 'modification_date']

class AddPlace(Resource):
    def get(self):
        return jsonify({'infolist':info_list})

    def post(self):
        geonameid = request.form.get('geonameid')
        name = request.form.get('name')
        asciiname = request.form.get('asciiname') 
        alternatenames = request.form.get('alternatenames')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        feature_class = request.form.get('feature_class')
        feature_code = request.form.get('feature_code')
        country_code = request.form.get('country_code')
        cc2 = request.form.get('cc2')
        admin1_code = request.form.get('admin1_code')
        admin2_code = request.form.get('admin2_code')
        admin3_code = request.form.get('admin3_code')
        admin4_code = request.form.get('admin4_code')
        population = request.form.get('population')
        elevation = request.form.get('elevation')
        dem = request.form.get('dem')
        timezone = request.form.get('timezone')
        modification_date = request.form.get('modification_date')

        info = [geonameid, name, asciiname, alternatenames, latitude, \
            longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, \
                admin3_code, admin4_code, population, elevation, dem, timezone, modification_date]
            
        if not all(info):
            msg = "****Veuillez remplir tous les champs. ****"
            return jsonify({"message":msg})
        else :
            location = fr(*info)
            db.session.add(location)
            db.session.commit()
            msg = '****{}({}) est bien ajoutée dans la base de données.****'.format(name, geonameid)
            return {"message":msg}, 201
        

class SearchPlaces(Resource):
    def get(self):
        city = request.args.get('name')
        if city is None:
            results = fr.query.all()
        else:
            results = fr.query.filter(fr.name.like("%" + city + "%") if city is not None else "").all()
        results_dico = {}
        for location in results:
            results_dico[location.geonameid] = {
                'geonameid' : location.geonameid,
                'name' : location.name,
                'latitude' : location.latitude,
                'longitude' : location.longitude
            }
        return jsonify(results_dico)

class PlaceInfoPage(Resource):
    def get(self, geonameid):
        geonameid = str(geonameid)
        location = fr.query.filter(fr.geonameid == geonameid).first()
        if not location:
            msg = f"La base de données n'a pas l'info de cette location ({geonameid})"
            return {"message":msg}, 404
        cityinfo = {
            "Geoname ID" : location.geonameid,
            "Name" : location.name,
            "Ascii Name" : location.asciiname,
            "Alternate Names" : location.alternatenames,
            "Latitude" : location.latitude,
            "Longitude" : location.longitude,
            "Feature class" : location.feature_class,
            "Feature code" : location.feature_code,
            "Country code" : location.country_code,
            "CC2" : location.cc2,
            "Admin1 code" : location.admin1_code,
            "Admin2 code" : location.admin2_code,
            "Admin3 code" : location.admin3_code,
            "Admin4 code" : location.admin4_code,
            "Population" : location.population,
            "Elevation" : location.elevation,
            "Dem" : location.dem,
            "Timezone" : location.timezone,
            "Modification date" : location.modification_date,
        }
        return jsonify({ geonameid : cityinfo })

    def put(self, geonameid):
        user_info = []
        db_info = []
        
        # les informations après changement de l'user
        for item in info_list:
            user_info.append(request.form.get(item))

        # les informations originales de db
        geonameid = str(geonameid)
        result = fr.query.filter(fr.geonameid == geonameid).first()
        if not result:
            msg = "La base de données n'a pas l'info de cette location ({})".format(geonameid)
            return {"message":msg}, 404

        for i in info_list:
            field_info = eval(f'result.{i}')
            db_info.append(field_info)

        for i in range(len(info_list)):
            if i == 0:
                if user_info[i] != db_info[i]:
                    msg = u"Désolé, le geonameid ne peut pas être changé."
                    return jsonify({"message":msg})
            else:
                if user_info[i] != db_info[i]:
                    db_info[i] = user_info[i]
        
        location_new_version = fr(*db_info)

        db.session.delete(result)
        db.session.add(location_new_version)
        db.session.commit()
        
        msg = '****Les informations de {}({}) est bien modifiées.****'.format(user_info[1], geonameid)
        return jsonify({"message":msg})


    def delete(self, geonameid):
        geonameid = str(geonameid)
        result = fr.query.filter(fr.geonameid == geonameid).first()
        if not result:
            msg = "La base de données n'a pas l'info de cette location ({})".format(geonameid)
            return {"message":msg}, 404
        cityname = result.name
        db.session.delete(result)
        db.session.commit()
        msg = '****{}({}) est supprimée.****'.format(cityname, geonameid)
        return jsonify({"message":msg})
        
        