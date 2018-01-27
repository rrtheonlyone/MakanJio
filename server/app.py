from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import *
import ast
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, '..', 'database', 'test.db')
db = SQLAlchemy(app)
api = Api(app)

# feedbacks = db.Table('feedbacks',
#     db.Column('feedbackId', db.ForeignKey('feedback.feedbackId'), primary_key=True),
#     db.Column('personId', db.ForeignKey('person.personId'), primary_key=True)
# )

class Person(db.Model):
    personId = db.Column(db.Integer, primary_key=True)
    personName = db.Column(db.String(120), nullable=False)
    personDesc = db.Column(db.String(2000), nullable=False)

    # receivedFeedbacks = db.relationship('Feedback', secondary=feedbacks, lazy='subquery',
    #     backref=db.backref('persons', lazy=True))
    writtenFeedbacks = db.relationship('Feedback', backref='feedbackAuthor', lazy=True)
    events = db.relationship('Food', backref='cook', lazy=True)

    def __repr__(self):
        return '<Hooman, id = %d, name = %s>' % (self.personId, self.personName)


attendees = db.Table('attendees',
    db.Column('foodId', db.ForeignKey('food.foodId'), primary_key=True),
    db.Column('attendeeId', db.ForeignKey('person.personId'), primary_key=True)
)


class Food(db.Model):
    foodId = db.Column(db.Integer, primary_key=True)
    cookId = db.Column(db.Integer, db.ForeignKey('person.personId'))
    locationLong = db.Column(db.Float)
    locationLat = db.Column(db.Float)
    price = db.Column(db.Integer) #In cents
    description = db.Column(db.String(2000))
    datetime = db.Column(db.Integer) #Datetime in yymmddhhmm
    cuisine = db.Column(db.String(150))
    quota = db.Column(db.Integer)

    attendees = db.relationship('Person', secondary=attendees, lazy='subquery',
        backref=db.backref('foods', lazy=True))
    feedbacks = db.relationship('Feedback', backref='foodEvent', lazy=True)

    def __repr__(self):
        return '<Fud, d = %d, cook = %d>' % (self.foodId, self.cookId)


class Feedback(db.Model):
    feedbackId = db.Column(db.Integer, primary_key=True)
    feedbackAuthorId = db.Column(db.Integer, db.ForeignKey('person.personId'))
    rating = db.Column(db.Integer)
    foodId = db.Column(db.Integer, db.ForeignKey('food.foodId'))
    message = db.Column(db.String(2000))

#ducttape
#returns a Dict
def getFeedback(id):
    o = {} #debug
    foodEvent = Food.query.filter_by(foodId=id).first()
    o["description"] = foodEvent.description
    cook = foodEvent.cook
    o["cook"] = cook.personName
    feedbacklist = []
    for feedback in foodEvent.feedbacks:
        feedbacklist.append({feedback.feedbackAuthor.personName: feedback.message})
    o['feedback'] = feedbacklist
    return o

class getAll(Resource):
    #Returns a list of dicts
    def get(self):
        o = []
        for event in Food.query.all():
            collect = {}
            collect['foodId'] = event.foodId
            collect['cookId'] = event.cookId
            collect['long'] = event.locationLong
            collect['lat'] = event.locationLat
            collect['price'] = event.price
            collect['description'] = event.description
            collect['datetime'] = event.datetime
            collect['cuisine'] = event.cuisine
            collect['quota'] = event.quota
            guestlist = []
            for attendee in event.attendees:
                guestlist.append(attendee.personName)
            collect['attendees'] = guestlist
            feedbacklist = []
            for feedback in event.feedbacks:
                feedbacklist.append({feedback.feedbackAuthor.personName: feedback.message})
            collect['feedback'] = feedbacklist
            o.append(collect)
        return o

    def post(self):
        pass

class getFood(Resource):
    def get(self, foodid):
        return getFeedback(foodid)

api.add_resource(getAll, '/cook/all')
api.add_resource(getFood, '/cook/<int:foodid>')

if __name__ == '__main__':
    app.run(debug=True)
