from flask import Flask, request, render_template, session, redirect, url_for
from flask_restful import Resource, Api

from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']

class AddPlace(Resource):
    def get(self):
        return {'infolist':['geonameid', 'name', 'asciiname', 'alternatenames', \
            'latitude', 'longitude', 'feature class', 'feature code', 'country code', 'cc2', \
            'admin1 code', 'admin2 code', 'admin3 code', 'admin4 code', 'population', \
            'elevation','dem','timezone','modification date' ]}

    def post(self):
        #########################有没有简化的方法
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
            
        if not all([geonameid, name, asciiname, alternatenames, latitude, \
            longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, \
                admin3_code, admin4_code, population, elevation, dem, timezone, modification_date]):
            msg = "****Veuillez remplir tous les champs. ****"
            return msg
        else :
            location = fr(geonameid, name, asciiname, alternatenames, latitude, \
            longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, \
                admin3_code, admin4_code, population, elevation, dem, timezone, modification_date)
            db.session.add(location)
            db.session.commit()
            msg = u'****{}({}) est bien ajoutée dans la base de données.****'.format(name, geonameid) ###########################怎么加入
            # return redirect(url_for('SearchPlaces'))
            return msg
        

class SearchPlaces(Resource):
    def get(self):
        ############### 这里页面跳转有问题，不知道是否还要考虑这个实现，以及如何实现
        city = request.args.get('name')
        # geoid = request.args.get('geonameid')
        # if geoid == None:

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
        print(len(results_dico.keys()))
        return results_dico
        # else:
        #     return redirect(url_for('PlaceInfoPage', geonameid = geoid)

class PlaceInfoPage(Resource):
    def get(self, geonameid):
        geonameid = str(geonameid)
        results = fr.query.filter(fr.geonameid == geonameid if geonameid is not None else "").all()
        for location in results:
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
        return { geonameid : cityinfo }

    def put(self, geonameid):
        # le formulaire de la part d'utilisateur 
        user_geonameid = request.form.get('geonameid')
        user_name = request.form.get('name')
        user_asciiname = request.form.get('asciiname') 
        user_alternatenames = request.form.get('alternatenames')
        user_latitude = request.form.get('latitude')
        user_longitude = request.form.get('longitude')
        user_feature_class = request.form.get('feature_class')
        user_feature_code = request.form.get('feature_code')
        user_country_code = request.form.get('country_code')
        user_cc2 = request.form.get('cc2')
        user_admin1_code = request.form.get('admin1_code')
        user_admin2_code = request.form.get('admin2_code')
        user_admin3_code = request.form.get('admin3_code')
        user_admin4_code = request.form.get('admin4_code')
        user_population = request.form.get('population')
        user_elevation = request.form.get('elevation')
        user_dem = request.form.get('dem')
        user_timezone = request.form.get('timezone')
        user_modification_date = request.form.get('modification_date')

        # les informations 
        geonameid = str(geonameid)
        results = fr.query.filter(fr.geonameid == geonameid if geonameid is not None else "").all()
        for location in results:
            if location.geonameid != user_geonameid :
                location.geonameid = user_geonameid 
            if location.name != user_name :
                location.name = user_name 
            if location.asciiname != user_asciiname :
                location.asciiname = user_asciiname 
            if location.alternatenames != user_alternatenames :
                location.alternatenames = user_alternatenames 
            if location.latitude != user_latitude :
                location.latitude = user_latitude 
            if location.longitude != user_longitude :
                location.longitude = user_longitude 
            if location.feature_class != user_feature_class :
                location.feature_class = user_feature_class 
            if location.feature_code != user_feature_code :
                location.feature_code = user_feature_code 
            if location.country_code != user_country_code :
                location.country_code = user_country_code 
            if location.cc2 != user_cc2 :
                location.cc2 = user_cc2 
            if location.admin1_code != user_admin1_code :
                location.admin1_code = user_admin1_code 
            if location.admin2_code != user_admin2_code :
                location.admin2_code = user_admin2_code 
            if location.admin3_code != user_admin3_code :
                location.admin3_code = user_admin3_code 
            if location.admin4_code != user_admin4_code :
                location.admin4_code = user_admin3_code 
            if location.population != user_population :
                location.population = user_population 
            if location.elevation != user_elevation :
                location.elevation = user_elevation 
            if location.dem != user_dem :
                location.dem = user_dem 
            if location.timezone != user_timezone :
                location.timezone = user_timezone
            if location.modification_date != user_modification_date :
                location.modification_date = user_modification_date
        db.session.commit()

        for location in results:
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
        
        msg = u'****Les informations de {}({}) est bien modifiées.****'.format(user_name, geonameid)
        return msg


    def delete(self, geonameid):
        geonameid = str(geonameid)
        results = fr.query.filter(fr.geonameid == geonameid if geonameid is not None else "").all()
        for city in results:
            cityname = city.name
            db.session.delete(city)
        db.session.commit()
        msg = u'****{}({}) est supprimée.****'.format(cityname, geonameid)
        # return redirect(url_for('SearchPlaces'))
        return msg