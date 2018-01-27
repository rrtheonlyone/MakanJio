# Change any details as necessary

from server.app import db
db.create_all()

from server.app import Person
from server.app import Food
from server.app import Feedback

person1 = Person(personId=1, personName='Alicia Amma', personDesc='I am a professional chef of 35 years. Having studied under Gordon Ramsey, I am confident that my food will tantalize your palate. Do message me to let me know of what sort of experience you would like to have, and I will specifically craft it for you.')
person2 = Person(personId=2, personName='Betty Barker', personDesc='Hi everybody! I am Betty and I am a home chef! Although I am a Singaporean by birth, I still love to travel the world and experience new cuisine! Only recently, I just came home from Lebanon and I loved their food, so I tried making them. I think they are delicious and would like to share them with you over dinner. Let us come together for a social experience.')
person3 = Person(personId=3, personName='Charlie Chao', personDesc='Uncle has been working in the industry for more than 20 years, and has been cooking for a lot of customers already. Uncle would like to cook for you at new stall in Bukit Gombak. Uncle look forward to meeting you!')

db.session.add(person1)
db.session.add(person2)
db.session.add(person3)
db.session.commit()

Person.query.all()

food1 = Food(foodId=1, cookId=2, locationLong=103.8, locationLat=1.34, price=1200, quota=10, datetime=1801231730, cuisine='Chinese Food', description='I want to practice my tze char. I will serve 3 vegetable dishes with rice. Let us bond over dinner!')
food2 = Food(foodId=2, cookId=1, locationLong=103.91, locationLat=1.32, price=4800, quota=4, datetime=1801231200, cuisine='Western Food', description='I am a chef of Western Food, I used to work for the Gordon Ramsay. We will be having some salads as starters, and some beef sirloin as a main. I will prepare the cuts to your liking of doneness. We will finish with a lava cake and some champaigne. This meal is best served with a family or couple.')
food3 = Food(foodId=3, cookId=2, locationLong=103.8, locationLat=1.34, price=2400, quota=6, datetime=1801251800, cuisine='Lebanese Food', description='Help me see if my Lebanese cooking is delicious! We start with some home made hummus, followed by an open faced sabih, and end with Kanafe as dessert. It will be a treat to try these awesome foods from the middle east!')
food4 = Food(foodId=4, cookId=3, locationLong=103.66, locationLat=1.14, price=800, quota=30, datetime=1801261800, cuisine='Chinese Food', description='To celebrate Uncle and his new Hawker stall opening, Uncle will cook tze char for 30 people who sign up first. We eat together and happy together!')

db.session.add(food1)
db.session.add(food2)
db.session.add(food3)
db.session.add(food4)
db.session.commit()

Food.query.all()

feedback1 = Feedback(feedbackId=1, feedbackAuthorId=3, rating=5, foodId=1, message='The food God only knows.')
feedback2 = Feedback(feedbackId=2, feedbackAuthorId=2, rating=3, foodId=1, message='Your food is not very nice.')
feedback3 = Feedback(feedbackId=3, feedbackAuthorId=3, rating=5, foodId=2, message='Spiritually awesome.')
feedback4 = Feedback(feedbackId=4, feedbackAuthorId=1, rating=4, foodId=2, message='The spices are good.')
feedback5 = Feedback(feedbackId=5, feedbackAuthorId=2, rating=5, foodId=1, message='The flowers in the rice are pretty.')

db.session.add(feedback1)
db.session.add(feedback2)
db.session.add(feedback3)
db.session.add(feedback4)
db.session.add(feedback5)
db.session.commit()

quit()
