from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from translate import *


app = Flask(__name__)
#!!! CORS dulu baru api
CORS(app)
api = Api(app)


rest = {
    'out1': 'request',
    'out2': 'complete',
    'out3': 'yey',
    'out4': 'gudd'
}

class Home(Resource):
    def get(self):
        return rest, 200

    def post(self):
        # ab = request.get_json()
        return request.get_json(), 200

class Prediccangry(Resource):
    def post(self):
        modeldir = "model/angry/Angry_model.h5"
        csvdir = "model/angry/angry.csv"
        txtdir = "model/angry/choruses.txt"
        # Input dari form
        dict_inpt = request.get_json()
        inp1 = dict_inpt['inp_1']
        inp2 = dict_inpt['inp_2']
        inp3 = dict_inpt['inp_3']
        inp4 = dict_inpt['inp_4']
        
        #menyiapkan output dari model
        hasil = translate(inp1,inp2,inp3,inp4,modeldir,csvdir,txtdir, wew=1)
        
        #kirim
        return hasil, 200

class Predicchappy(Resource):
    def post(self):
        modeldir = "model/happy/happy_model.h5"
        csvdir = "model/happy/happy.csv"
        txtdir = "model/happy/choruses.txt"
        # Input dari form
        dict_inpt = request.get_json()
        inp1 = dict_inpt['inp_1']
        inp2 = dict_inpt['inp_2']
        inp3 = dict_inpt['inp_3']
        inp4 = dict_inpt['inp_4']
        
        #menyiapkan output dari model
        hasil = translate(inp1,inp2,inp3,inp4,modeldir,csvdir,txtdir, wew=2)
        
        #kirim
        return hasil, 200

class Prediccsad(Resource):
    def post(self):
        modeldir = "model/sad/sad_model.h5"
        csvdir = "model/sad/sad.csv"
        txtdir = "model/sad/choruses.txt"
        # Input dari form
        dict_inpt = request.get_json()
        inp1 = dict_inpt['inp_1']
        inp2 = dict_inpt['inp_2']
        inp3 = dict_inpt['inp_3']
        inp4 = dict_inpt['inp_4']
        
        #menyiapkan output dari model
        hasil = translate(inp1,inp2,inp3,inp4,modeldir,csvdir,txtdir, wew=3)
        
        #kirim
        return hasil, 200

api.add_resource(Home, '/')
api.add_resource(Prediccangry, '/predict/angry')
api.add_resource(Predicchappy, '/predict/happy')
api.add_resource(Prediccsad, '/predict/sad')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
