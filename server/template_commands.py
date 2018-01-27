# Change any details as necessary

from server.app import db
db.create_all()

from server.app import Person
from server.app import Food
from server.app import Feedback

person1 = Person(personId=1, personName='Person 1')
person2 = Person(personId=2, personName='Person 2')
person3 = Person(personId=3, personName='Person 3')

db.session.add(person1)
db.session.add(person2)
db.session.add(person3)
db.session.commit()

Person.query.all()

food1 = Food(foodId=1, cookId=3, locationLong=105, locationLat=1.16, price=1000, description='Ubiquitous')
food2 = Food(foodId=2, cookId=2, locationLong=105.2, locationLat=1.17, price=890, description='Not so ubiquitous')

db.session.add(food1)
db.session.add(food2)
db.session.commit()

Food.query.all()

feedback1 = Feedback(feedbackId=1, feedbackAuthorId=1, foodId=1, message='The foodGod only knows')
feedback2 = Feedback(feedbackId=2, feedbackAuthorId=2, foodId=1, message='Your fuudois shit')

db.session.add(feedback1)
db.session.add(feedback2)
db.session.commit()

def getDetails(id):
    foodEvent = Food.query.filter_by(foodId=id).first()
    print("Description: " + foodEvent.description)
    cook = foodEvent.cook
    print("Cook name: " + cook.personName)
    print("Feedback about the event")
    for feedback in foodEvent.feedbacks:
        print("From " + feedback.feedbackAuthor.personName + ": " + feedback.message)

                                        
getDetails(1)
