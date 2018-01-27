from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import *
import ast
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
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


#    0     1      2   3    4        5          6       7      8       9        10
# foodId cookId long lat price description datetime cuisine quota attendees feedback
class getAll(Resource):
    #Returns a list of dicts
    def get(self):
        o = []
        for event in Food.query.all():
            collect = []
            collect.append(event.foodId)
            collect.append(event.cookId)
            collect.append(event.locationLong)
            collect.append(event.locationLat)
            collect.append(event.price)
            collect.append(event.description)
            collect.append(event.datetime)
            collect.append(event.cuisine)
            collect.append(event.quota)
            guestlist = []
            for attendee in event.attendees:
                guestlist.append(attendee.personName)
            collect.append(guestlist)
            feedbacklist = []
            for feedback in event.feedbacks:
                feedbacklist.append([feedback.feedbackAuthor.personName, feedback.message, feedback.rating])
            collect.append(feedbacklist)
            o.append(collect)
        return o

    def post(self):
        pass


#       0       1     2       3
# description chef feedback score
class getFood(Resource):
    def get(self, id):
        # Output is desc, chef, feedback in that order
        o = []
        foodEvent = Food.query.filter_by(foodId=id).first()
        o.append(foodEvent.description)
        cook = foodEvent.cook
        o.append(cook.personName)
        feedbacklist = []
        overallscore = 0 #This will be a 2 digit number = 10*actual score
        for feedback in foodEvent.feedbacks:
            feedbacklist.append([feedback.feedbackAuthor.personName, feedback.message, feedback.rating])
            overallscore += feedback.rating
        o.append(feedbacklist)
        if len(feedbacklist) == 0:
            o.append(0)
        else:
            o.append(10*overallscore/len(feedbacklist))
        return o


#    0          1         2
# chefname description feedbacks overallrating
class getChef(Resource):
    def get(self,id):
        o = []
        currChef = Person.query.filter_by(personId=id).first()
        o.append(currChef.personName)
        o.append(currChef.personDesc)
        feedbacklist = []
        overallscore = 0 #This will be a 2 digit number = 10*actual score
        # name, message, rating in that order
        for feedback in Feedback.query.filter_by(cookId=id):
            feedbacklist.append([feedback.feedbackAuthor.personName, feedback.message, feedback.rating])
            overallscore += feedback.rating
        o.append(feedbacklist)
        if len(feedbacklist) == 0:
            o.append(0)
        else:
            o.append(10*overallscore/len(feedbacklist))
        return o



api.add_resource(getAll, '/event')
api.add_resource(getFood, '/event/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
