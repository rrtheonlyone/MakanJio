# Run this from your flask shell

m server.app import db
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

food1 = Food(foodId=1, cookId=1, locationLong=0, locationLat=0, price=1000,
description='Ubiquitous')
food2 = Food(foodId=2, cookId=2, locationLong=0, locationLat=0, price=2000,
description='Rare')

db.session.add(food1)
db.session.add(food2)
db.session.commit()

Food.query.all()

feedback1 = Feedback(feedbackId=1, feedbackerId=1, message='The food God only knows')
feedback2 = Feedback(feedbackId=2, feedbackerId=2, message='Your fuudo is shit')

db.session.add(feedback1)
db.session.add(feedback2)
db.session.commit()

person3.feedbacks.append(feedback1)
person3.feedbacks.append(feedback2)

feedbacks = Person.query.filter(personId=3).first().feedbacks
