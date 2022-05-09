# ============================================
# Title: Exercise 9.3
# Author: Professor Krasso
# Date: 9 May 2022
# Modified By: Joel Hartung
# Description: hartung-user-update.py
# Code Attribution: Code from the Exercise 9.3 document
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

# update user document
db.users.update_one(
    {"employee_id": "00000001"},
    {
        "$set": {
            "email": "jvhartung@my365.bellevue.edu"
        }
    }
)

# query users collection using "find_one()" method & print returned document
pprint.pprint(db.users.find_one({"employee_id": "00000001"}))
