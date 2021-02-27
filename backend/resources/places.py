from flask import Flask, request, render_template, session, redirect, url_for
from flask_restful import Resource, Api

from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']

geonames = {
    '2659815':{
        'geonameid':'2659086',
        'name': 'Lucelle',
        'asciiname': 'Lucelle',
        'latitude': '46.30352',
        'longitude': '6.82838'
    },
    '2659086':{
        'geonameid':'2659086',
        'name': 'Col de Recon',
        'asciiname': 'Col de Recon',
        'latitude': '47.41667',
        'longitude': '7.5'
    }
}

class AddPlace(Resource):
    def get(self):
        return {'infolist':['geonameid', 'name', 'asciiname', 'alternatenames', \
            'latitude', 'longitude', 'feature class', 'feature code', 'country code', 'cc2', \
            'admin1 code', 'admin2 code', 'admin3 code', 'admin4 code', 'population', \
            'elevation','dem','timezone','modification date' ]}

    def post(self):
        #########################有没有简化的方法
        ###########有问题，错误码400
        if not request.form['geonameid'] or not request.form['name'] or not request.form['asciiname'] or not request.form['alternatenames'] or not request.form['latitude'] or not request.form['longitude'] or not request.form['feature_class'] or not request.form['feature_code'] or not request.form['country_code'] or not request.form['cc2'] or not request.form['admin1_code'] or not request.form['admin2_code'] or not request.form['admin3_code'] or not request.form['admin4_code'] or not request.form['population'] or not request.form['elevation'] or not request.form['dem'] or not request.form['timezone'] or not request.form['modification_date']:
            msg = "****Please enter all the fields****"
            return msg
        else :
            location = fr(request.form['geonameid'],request.form['name'], request.form['asciiname'], request.form['alternatenames'], request.form['latitude'], request.form['longitude'], request.form['feature_class'], request.form['feature_code'], request.form['country_code'], request.form['cc2'], request.form['admin1_code'], request.form['admin2_code'], request.form['admin3_code'],request.form['admin4_code'], request.form['population'],request.form['elevation'], request.form['dem'],request.form['timezone'], request.form['modification_date'])
            db.session.add(location)
            db.session.commit()
            msg = '****The location was successfully added.****'  ###########################怎么加入
            return redirect(url_for('SearchPlaces'))
        


##############################################
class SearchPlaces(Resource):
    def get(self):
        ############### 这里页面跳转有问题，不知道是否还要考虑这个实现，以及如何实现
        city = request.args.get('name')
        geoid = request.args.get('geonameid')
        if geoid == None:
            if city is None:
                city = " "
            results = fr.query.filter(fr.name.like("%" + city + "%") if city is not None else "").all()
            results_dico = {}
            for location in results:
                results_dico[location.geonameid] = {
                    'geonameid' : location.geonameid,
                    'name' : location.name,
                    'latitude' : location.latitude,
                    'longitude' : location.longitude
                }
            return results_dico
        else:
            return redirect(url_for('PlaceInfoPage', geonameid = geoid))
    
    # def post(self):
    #     name_dico = {}
    #     for location in fr.query.all()[:5]:
    #         print(location.name)
    #         name_dico[location.name] = location.geonameid
    #     return name_dico

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

    def put(self):
        return "update the info"

    def delete(self, geonameid):
        geonameid = str(geonameid)
        results = fr.query.filter(fr.geonameid == geonameid if geonameid is not None else "").all()
        db.session.delete(results)
        db.session.commit()
        msg = '****Cette location est supprimée.****'
        # return redirect(url_for('SearchPlaces'))
        return msg