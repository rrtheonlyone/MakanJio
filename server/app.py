from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

import ast

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_API'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
api = Api(app)

class Food(db.Model):
    foodid = db.Column(db.Integer, primary_key=True)
    cook = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    placeLong = db.Column(db.Float, nullable=False)
    placeLat = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# This is for people who are particiapting in the dining
class FoodPeople(db.Model):
    foodid = db.Column(db.Integer, ForeignKey('Food.foodid'), nullable=False)
    people = db.Column(db.String(120), nullable=False)

class FeedbackPeople(db.Model):
    foodid = db.Column(db.Integer, ForeignKey('Food.foodid'), nullable=False)
    people = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class Sorting(Resource):
    def get(self):
        return "This is the sorting problem answer"

    def post(self):
        return qsort(request.get_json(force=True))

api.add_resource(Sorting, '/sort')

if __name__ == '__main__':
    app.run(debug=True)
