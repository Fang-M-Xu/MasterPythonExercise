import pymongo
from flask import Flask,  Response, request
from bson.objectid import ObjectId
import json,os
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students_fakedata ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')

MONGODB_URL='mongodb+srv://morganx:QWEasd123@day30python.paqby1j.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(MONGODB_URL)
db = client['thirty_days_python']

@app.route('/app/v1/students',methods=['GET'])
def students():
    students = db.student.find()
    return Response(json.dumps(students),mimetypes = 'application/json')

@app.route('/app/v1/students/<id>',methods=['GET'])
def single_student(id):
    students = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(students),mimetype = 'application/json')

@app.route('/app/v1/students', methods=['POST'])
def create_student():
    name = request.get_json().get('name')
    city = request.get_json().get('city')
    country = request.get_json().get('country')
    skills = request.get_json().get('skills')
    bio = request.get_json().get('bio')
    birthyear = request.get_json().get('birthyear')
    created_at = datetime.now()
    student = {
        'name':name,
        'country':country,
        'city':city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.insert_one(student)
    return 'success'


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
    # pass