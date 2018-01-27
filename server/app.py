from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

import ast

from LZM import compress 
from RLE import compress1
from WDE import compressWDE
from BusyTrain import busybody
from sort import qsort
from EmptyArea import rectangle, circle 
from jewellery_heist import fakeknapsack
from releaseSchedule import scheduler
from horse import horsenipples

app = Flask(__name__)
api = Api(app)

class Sorting(Resource):
    def get(self):
        return "This is the sorting problem answer"

    def post(self):
        return qsort(request.get_json(force=True))


class StringCompression(Resource):
    def get(self, mode):
        return "This is the String Compression Problem"

    def post(self, mode):
        json_data = request.get_json(force=True)
        string_value = json_data['data']

        if(mode == "LZW"):
            answer = compress(string_value)
        elif(mode == "RLE"):
            answer = compress1(string_value)
        else:
            answer = compressWDE(string_value)

        return answer

class JewelleryHeist(Resource):
    def get(self):
        return "This is the Jewellery Heist Problem"

    def post(self):
        json_data = request.get_json(force=True)
        weight = json_data["maxWeight"]
        vault = json_data["vault"]

        answer = fakeknapsack(vault, weight)
        answer_json = {"heist": answer}
        return jsonify(answer_json)  

class HorseRacing(Resource):
    def get(self):
        return "This is the Horse Racing Problem"

    def post(self):
        json_data = request.get_json(force=True)
        data = json_data['data']

        answer = horsenipples(data)

        return jsonify(answer)

class ReleaseScheduler(Resource):
    def get(self):
        return "This is the Release Scheduler Problem"

    def post(self):
        raw_list = request.get_data()
        raw_list_string = raw_list.decode("utf-8")
        list_string = ast.literal_eval(raw_list_string)
        answer = scheduler(list_string)
        return answer

class TrainPlanner(Resource):
    def get(self):
        return "This is the Train Planner Problem"

    def post(self):
        json_data = request.get_json(force=True)
        destination = json_data['destination']
        stations = json_data['stations']
        answer = busybody(destination, stations)

        return answer

class CalculateEmptyArea(Resource):
    def get(self):
        return "This is the Empty Area Problem"

    def post(self):
        json_data = request.get_json(force=True)
        answer = 0
        
        con_X = json_data["container"]["coordinate"]["X"]
        con_Y = json_data["container"]["coordinate"]["Y"]
        con = [con_X, con_Y]

        condim_width = json_data["container"]["width"]
        condim_height = json_data["container"]["height"]
        condim = [condim_width, condim_height]

        if "rectangle" in json_data:
            sha_X = json_data["rectangle"]["coordinate"]["X"]
            sha_Y = json_data["rectangle"]["coordinate"]["Y"]
            sha = [sha_X, sha_Y]

            shadim_width = json_data["rectangle"]["width"]
            shadim_height = json_data["rectangle"]["height"]
            shadim = [shadim_width, shadim_height]

            answer = rectangle(con, condim, sha, shadim)

        if "square" in json_data:
            sha_X = json_data["square"]["coordinate"]["X"]
            sha_Y = json_data["square"]["coordinate"]["Y"]
            sha = [sha_X, sha_Y]

            shadim_width = json_data["square"]["width"]
            shadim = [shadim_width, shadim_width]
            
            answer = rectangle(con, condim, sha, shadim)

        if "circle" in json_data:
            sha_X = json_data["circle"]["center"]["X"]
            sha_Y = json_data["circle"]["center"]["Y"]
            sha = [sha_X, sha_Y]

            radius = json_data["circle"]["radius"]

            answer = circle(con, condim, sha, radius)

        return answer


api.add_resource(Sorting, '/sort')
api.add_resource(StringCompression, '/stringcompression/<mode>')
api.add_resource(TrainPlanner, '/trainPlanner')
api.add_resource(CalculateEmptyArea, '/calculateemptyarea')
api.add_resource(JewelleryHeist, '/heist')
api.add_resource(ReleaseScheduler, '/releaseSchedule')
api.add_resource(HorseRacing, '/horse-racing')

if __name__ == '__main__':
    app.run(debug=True)