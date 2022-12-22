'''

    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
    Delete one of the items in the dictionary
    Delete one of the dictionaries

'''
dog = dict()
dog['name'] = 'DoDo'
dog['color'] = 'Black'
dog['breed'] = 'Chinese Rural dog'
dog['legs'] = 4
dog['age'] = 2
print(dog)
student={
    'first_name':'Jack',
    'last_name':'Potter',
    'gender':'M',
    'age':22,
    'marital status':False,
    'skills':['Python','Java','HTML5'],
    'country':'China',
    'city':'Yunnan',
    'address':'New Building'
}
print(student, len(student))
skills=student.get('skills')
print(skills,type(skills))
skills.append('HTTP')
print(student)
print(student.keys())
print(student.values())

student_tuple=student.items()
print(student_tuple)

student.popitem()
print(student)
del student