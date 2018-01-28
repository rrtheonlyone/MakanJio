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
    datetime = db.Column(db.String(150)) #Datetime in yymmddhhmm
    cuisine = db.Column(db.String(150))
    quota = db.Column(db.Integer)
    title = db.Column(db.String(150))

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


#    0     1      2   3    4     5      6       7      8       9        10     11
# foodId cookId long lat price desc datetime cuisine quota attendees feedback title
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
            collect.append(event.title)
            o.append(collect)
        return o

    def post(self):
        pass


def eventmethod(event):
    collect = []
    collect.append(event.foodId)
    collect.append(event.cookId)
    collect.append(event.locationLong)
    collect.append(event.locationLat)
    collect.append(event.price / 100)
    collect.append(event.description)
    collect.append(event.datetime)
    collect.append(event.cuisine)
    collect.append(event.quota)
    guestlist = []
    for attendee in event.attendees:
        guestlist.append(attendee.personName)
    collect.append(guestlist)
    feedbacklist = []
    overallscore = 0
    for feedback in event.feedbacks:
        feedbacklist.append([feedback.feedbackAuthor.personName, feedback.message, feedback.rating])
        overallscore += feedback.rating
    collect.append(feedbacklist)
    collect.append(event.title)
    if len(feedbacklist) == 0:
        collect.append(0)
    else:
        collect.append(10*overallscore/len(feedbacklist))
    collect.append(Person.query.filter_by(personId=event.cookId).first().personName)
    return collect


class getFood(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('personId', type = int, location = 'json')
        
    def get(self, fudId):
        # Output is same order as above, index 12 is score
        event = Food.query.filter_by(foodId=fudId).first()
        return eventmethod(event)

    # def post(self, id):
    #     print("THE ID: " + str(id))
    #     return {'Status': 200}

    def post(self, fudId):
        parser = reqparse.RequestParser()
        parser.add_argument('personId', type=int)

        args = parser.parse_args()

        personId = args['personId']
        event = fudId
        dude = Person.query.filter_by(personId=personId).first()
        event = Food.query.filter_by(foodId=event).first()
        event.attendees.append(dude)
        db.session.add(event)
        db.session.commit()
        return {'Status': 200}


#    0          1          2           3            4
# chefname description feedbacks overallrating listofevents
class getChef(Resource):
    def get(self,chefId):
        o = []
        currChef = Person.query.filter_by(personId=chefId).first()
        o.append(currChef.personName)
        o.append(currChef.personDesc)
        feedbacklist = []
        listevents = []
        overallscore = 0 #This will be a 2 digit number = 10*actual score
        # name, message, rating in that order

        for foodEvent in currChef.events:
            listevents.append(eventmethod(foodEvent))
            for feedback in foodEvent.feedbacks:
                feedbacklist.append([
                    feedback.feedbackAuthor.personName,
                    feedback.message, 
                    feedback.rating])
                overallscore += feedback.rating

        # for feedback in Feedback.query.filter_by(feedbackAuthorId=id): #JesusChrist
        #     feedbacklist.append([feedback.feedbackAuthor.personName, feedback.message, feedback.rating])
        #     overallscore += feedback.rating
        
        o.append(feedbacklist)
        if len(feedbacklist) == 0:
            o.append(0)
        else:
            o.append(10*overallscore/len(feedbacklist))
        o.append(listevents)

        return o


class postComment(Resource):
    def post(self, eventId):
        parser = reqparse.RequestParser()
        parser.add_argument('authorId', type=int)
        parser.add_argument('rating', type=int)
        parser.add_argument('description', type=str)

        args = parser.parse_args()

        feedbackId = len(Feedback.query.all()) + 1
        authorId = args['authorId']
        rating = args['rating']
        description = args['description']

        fb = Feedback(feedbackId=feedbackId, feedbackAuthorId=authorId,
            rating=rating, foodId=eventId, message=description)
        db.session.add(fb)
        db.session.commit()
        return {'Status' : 200}

class reset(Resource):
    def get(self):
        # KILL
        Feedback.query.delete()
        Food.query.delete()
        Person.query.delete()

        # REVIVE
        person1 = Person(personId=1, personName='Alicia Amma', personDesc='I am a professional chef of 35 years. Having studied under Gordon Ramsey, I am confident that my food will tantalize your palate. Do message me to let me know of what sort of experience you would like to have, and I will specifically craft it for you.')
        person2 = Person(personId=2, personName='Betty Barker', personDesc='Hi everybody! I am Betty and I am a home chef! Although I am a Singaporean by birth, I still love to travel the world and experience new cuisine! Only recently, I just came home from Lebanon and I loved their food, so I tried making them. I think they are delicious and would like to share them with you over dinner. Let us come together for a social experience.')
        person3 = Person(personId=3, personName='Charlie Chao', personDesc='Uncle has been working in the industry for more than 20 years, and has been cooking for a lot of customers already. Uncle would like to cook for you at new stall in Bukit Gombak. Uncle look forward to meeting you!')

        db.session.add(person1)
        db.session.add(person2)
        db.session.add(person3)
        db.session.commit()

        food1 = Food(foodId=1, cookId=2, locationLong=103.866, locationLat=1.336, price=1200, quota=10, datetime="23rd Jan 2018, 1730hrs", cuisine='Chinese Food', description='I want to practice my tze char. I will serve 3 vegetable dishes with rice. Let us bond over dinner!', title='Simple Chinese Tze Char Dinner')
        food2 = Food(foodId=2, cookId=1, locationLong=103.8755, locationLat=1.334, price=4800, quota=4, datetime="24th Jan 2018, 1800hrs", cuisine='Western Food', description='I am a chef of Western Food, I used to work for the Gordon Ramsay. We will be having some salads as starters, and some beef sirloin as a main. I will prepare the cuts to your liking of doneness. We will finish with a lava cake and some champaigne. This meal is best served with a family or couple.', title='Dining with a Professional Chef')
        food3 = Food(foodId=3, cookId=2, locationLong=103.875, locationLat=1.329, price=2400, quota=6, datetime="25th Jan 2018, 1800hrs", cuisine='Lebanese Food', description='Help me see if my Lebanese cooking is delicious! We start with some home made hummus, followed by an open faced sabih, and end with Kanafe as dessert. It will be a treat to try these awesome foods from the middle east!', title='Lebanese is awesome!')
        food4 = Food(foodId=4, cookId=3, locationLong=103.866, locationLat=1.33, price=800, quota=30, datetime="26th Jan 2018, 1800hrs", cuisine='Chinese Food', description='To celebrate Uncle and his new Hawker stall opening, Uncle will cook tze char for 30 people who sign up first. We eat together and happy together!', title="Uncle's Open House!")

        db.session.add(food1)
        db.session.add(food2)
        db.session.add(food3)
        db.session.add(food4)
        db.session.commit()

        feedback1 = Feedback(feedbackId=1, feedbackAuthorId=3, rating=5, foodId=1, message='The food God only knows.')
        feedback2 = Feedback(feedbackId=2, feedbackAuthorId=2, rating=3, foodId=1, message='Your food is not very nice.')
        feedback3 = Feedback(feedbackId=3, feedbackAuthorId=3, rating=5, foodId=2,
        message='Spiritually awesome.')

        feedback4 = Feedback(feedbackId=4, feedbackAuthorId=1, rating=4, foodId=2, message='The spices are good.')
        feedback5 = Feedback(feedbackId=5, feedbackAuthorId=2, rating=5, foodId=1, message='The flowers in the rice are pretty.')

        db.session.add(feedback1)
        db.session.add(feedback2)
        db.session.add(feedback3)
        db.session.add(feedback4)
        db.session.add(feedback5)
        db.session.commit()

        food3.attendees.append(person1)
        db.session.add(food3)
        db.session.commit()
		
class addOn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('desc', type=str)

        args = parser.parse_args()
        
        longitude = 103.903
        latitude = 1.398
        foodId = 5
        cookId = 2
        price = 3000
        quota = 5
        datetime = "24th Jan 2018, 1900hrs"
        cuisine = "Indian"
        title = args['title']
        description = args['desc']
        
        newFood = Food(foodId=foodId, cookId=cookId, locationLong=longitude,
            locationLat = latitude, price=price, quota=quota, datetime=datetime,
            cuisine=cuisine, description=description, title=title)

        db.session.add(newFood)
        db.session.commit()

        return {'Status' : 200}

api.add_resource(getAll, '/event')
api.add_resource(getFood, '/event/<int:fudId>')
api.add_resource(getChef, '/chef/<int:chefId>')
api.add_resource(postComment, '/feedback/<int:eventId>')
api.add_resource(reset, '/reset')
api.add_resource(addOn, '/add')

if __name__ == '__main__':
    app.run(debug=True)
