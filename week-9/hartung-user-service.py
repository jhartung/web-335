# ============================================
# Title: Exercise 9.2
# Author: Professor Krasso
# Date: 9 May 2022
# Modified By: Joel Hartung
# Description: hartung-user-service.py
# Code Attribution: Code from the Exercise 9.2 document
# ============================================


# import statements
from pymongo import MongoClient
import pprint
import datetime

# connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# create a new user document
user = {
    "first_name": "Jean-Claude",
    "last_name": "Van Damme",
    "email": "jcvd@mail.com",
    "employee_id": "00000001",
    "date_created": datetime.datetime.utcnow()
}

# insert new user document
user_id = db.users.insert_one(user).inserted_id

# output auto-generated user_id
print(user_id)

# query users collection using "find_one()" method & print returned document
pprint.pprint(db.users.find_one({"employee_id": "00000001"}))
