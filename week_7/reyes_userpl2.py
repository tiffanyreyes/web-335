#===========================================================================================
#; Title: reyes-userpl2.py
#; Author: Tiffany Reyes
#; Date: 6 July 2023
#; Description: Python with MongoDB Pt 2
#;==========================================================================================

# import the MongoClient
from pymongo.mongo_client import MongoClient
from pprint import pprint
from datetime import datetime

# build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.paicaia.mongodb.net/?retryWrites=true&w=majority")

# specify database to connect to
db = client['web335DB']

# specify collection to connect to
col = db["users"]

# creating a new user document
inserted_user = col.insert_one({
    "firstName": "Antonio",
    "lastName": "Vivaldi",
    "employeeId": "1014",
    "email": "vivaldia@me.com",
    "dateCreated": datetime.today()
})

# display new document
user = col.find_one( { "_id": inserted_user.inserted_id } )
print(user)

# update email address of document
myquery = { "email": "vivaldia@me.com" }
newvalues = { "$set": { "email": "avivaldi@me.com" } }

col.update_one(myquery, newvalues)

# display user document after update
user = col.find_one( { "email": "avivaldi@me.com" } )
print(user)

# deleting user document
col.delete_one( { "_id": inserted_user.inserted_id } )

# display deleted user document
results = col.find_one( { "_id": inserted_user.inserted_id } )
print(results)