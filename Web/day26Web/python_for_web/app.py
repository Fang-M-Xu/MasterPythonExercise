from flask import Flask,render_template
import pymongo
import os
from bson.objectid import ObjectId

MONGODB_URI = 'mongodb+srv://morganx:QWEasd123@day30python.paqby1j.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client.thirty_days_python
# db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
# print(client.list_database_names())

# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for item in students:
#     db.students.insert_one(item)
# print(client.list_database_names())

# student = db.students.find_one({'_id':ObjectId('63a7dcf9287f9f35d7e7b1ca')})
# print(student)
# students_col = db.students.find({},{"_id":0,"name":1,"country":1})
# for item in students_col:
#     print(item)

# students_lst = db.students.find()
# for item in students_lst:
#     print(item)

# query={"country":"Finland"}
# students=db.students.find(query)
# for student in students:
#     print(student)

query = {"age":{"$gt":30}}
students = db.students.find(query).limit(2)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    # port = int(os.environ.get("PORT", 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)
    pass