from flask import Flask,current_app, jsonify, make_response, Response,  Blueprint, abort,render_template, request, redirect,render_template_string, url_for, send_from_directory
from flask_restful import Api, Resource, reqparse,wraps
import uuid
import json
from notepad_model import *

class NotepadsAPI(Resource):
    def __init__(self):
        self.notepads = Notepad()
    def get(self):
        s = self.notepads.list()
        return jsonify(s)
    def post(self):
        try:
            fromclients = request.get_json()
        except:
            fromclients=dict()
        s = self.notepads.create(fromclients)
        return jsonify(s)

class NotepadAPIMetrics(Resource):
    def __init__(self):
        self.notepads = Notepad()
    def get(self):
        s = self.notepads.metrics()
        return jsonify(s)


class NotepadAPI(Resource):
    def __init__(self):
        self.notepads = Notepad()
    def get(self,id):
        s = self.notepads.read(id)
        return jsonify(s)
    def put(self,id):
        try:
            fromclients = request.get_json()
        except:
            fromclients = dict()
        s = self.notepads.update(id,fromclients)
        return jsonify(s)
    def delete(self,id):
        s = self.notepads.delete(id)
        return jsonify(s)



def get_flask(name):
    app = Flask(name)
    app.secret_key = b'781231casda9871293812h3'
    return app

def get_blueprint(nama):
    app = get_flask(__name__)
    @app.route('/')
    def index():
        return "please use api endpoint"
    api = Api(app)
    api.add_resource(NotepadsAPI,'/notepads',endpoint='notepads')
    api.add_resource(NotepadAPI,'/notepads/<id>',endpoint='notepad')
    api.add_resource(NotepadAPIMetrics,'/notepads/metrics',endpoint='notepadsmetric')
    return app

app = get_blueprint(__name__)
if __name__=='__main__':
    app.run(host='0.0.0.0', port=32000, debug=True)