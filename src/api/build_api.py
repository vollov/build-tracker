# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request
from flask.ext.restful import  Resource

from domain.build import Build
from orm.database import db_session
from utils.json_utils import JsonUtil
import json

from datetime import datetime

class BuildApi(Resource):
    def get(self, oid):
        build = Build.query.filter(Build.id == oid).first()
        return Response(JsonUtil.objectToJson(build), mimetype='application/json')
    
    def delete(self, oid):
        try:
            Build.query.filter(Build.id == oid).delete()
            db_session.commit()
            return True, 204
        except Exception as e:
            print e
            return '', 500
        
    def put(self, oid):
        build = json.loads(request.data, object_hook=Build.decode)

        try:
            build = db_session.merge(build)
            db_session.commit()
        except Exception as e:
           #TODO: log exception
           print e
        return JsonUtil.objectToJson(build), 201
    
class BuildListApi(Resource):
    def get(self):
        try:
            builds = Build.query.all()
            return Response(JsonUtil.listToJson(builds), mimetype='application/json')
        except Exception as e:
            print e
            return '', 500
        
    def post(self):
        build = json.loads(request.data, object_hook=Build.decode)
        try:
            db_session.add(build)
            db_session.commit()
        except Exception as e:
            print e
        return JsonUtil.objectToJson(build), 201
#         return '', 201