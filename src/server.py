# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext import restful
from orm.database import db_session
import re

app = Flask(__name__)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

api = restful.Api(app)

@app.teardown_request
def shutdown_session(exception=None):
    parser = re.compile(r'^/api/.*')
    match_object = parser.match(request.path)
    if match_object:
        db_session.remove()
    
############################################################
# global view mapping end
############################################################

def register_blueprints(application, api):
    #register angularjs front end
    from front_end import front
    application.register_blueprint(front)
    
    from api.build_api import BuildApi, BuildListApi
    api.add_resource(BuildListApi, '/api/builds')
    api.add_resource(BuildApi, '/api/builds/<int:oid>')
    
register_blueprints(app, api)

if __name__ == '__main__':
    app.run(debug=False)