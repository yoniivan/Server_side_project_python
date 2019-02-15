from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

camera = {
    "speed": "1000",
    "f": "4.5",
    "iso": "1800"
}

arduino = {
    "light_sensor": "10",
}

android = {
"Water_Drop": "10"
}

light_sensor = {}

def generateParams(loght_sensor):
    speed = "1"
    f = float(camera['f']) + (float(loght_sensor) * 0)
    iso = int(loght_sensor)
    camera['speed'] = speed
    camera['f'] = f
    camera['iso'] = iso


class Camera(Resource):
    def post(self):
        all_args = request.json
        print(all_args)

    def put(self):
        light_sensor = request.args.get('aaa')
        print(light_sensor)

    def get(self):
        generateParams(arduino['light_sensor'])
        return jsonify(camera)

class Arduino(Resource):
    def post(self):
        light_sensor = request.json
        light_sensor = light_sensor['light_sensor']
        arduino['light_sensor'] = light_sensor
        print(arduino['light_sensor'])


class Android(Resource):
    def put(self):
        water = request.json
        android.update(water)
        print(android)
        return jsonify(android)

    def get(self):
        print(android)
        return jsonify(android)


api.add_resource(Arduino, '/arduino')
api.add_resource(Android,'/android/')
api.add_resource(Camera, '/camera')

app.run(host='192.168.1.16', port=5000)
