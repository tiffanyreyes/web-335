#===========================================================================================
#; Title: reyes-userpl.py
#; Author: Tiffany Reyes
#; Date: 29 June 2023
#; Description: Python with MongoDB
#;==========================================================================================

# import the MongoClient
from pymongo.mongo_client import MongoClient
from pprint import pprint

# build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.paicaia.mongodb.net/?retryWrites=true&w=majority")

# specify database to connect to
db = client['web335DB']

# loop to iterate over all users and display with pretty print
for user in db.users.find({}):
    pprint(user)

# find employeeId and then display in pretty print
pprint(db.users.find_one({ "employeeId": "1011" }))

# find lastName and then display in pretty print
pprint(db.users.find_one({ "lastName": "Mozart" }))

