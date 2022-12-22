'''
Exercises: Level 1

    Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.

user = int(input("Enter your age: "))
if user >= 18:
    print("You are old enough to learn to drive.")
else:
    diff = 18 - user
    print(f"You need {diff} more years to learn to drive.")
'''
'''
    Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

    Enter your age: 30
    You are 5 years older than me.

your_age = int(input("Enter your age: "))
my_age = 25
if your_age > my_age:
    if your_age - my_age == 1:
        print("Our age are close")
    else:
        diff = your_age - my_age
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    print("YOu are younger than me.")
else:
    print("We are same age.")
'''
'''
    Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3

num1 = input("Enter number one: ")
num2 = input("Enter number two: ")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
'''
'''
### Exercises: Level 2

    Write a code which gives grade to students according to theirs scores:

    80-100, A
    70-79, B
    60-69, C
    50-59, D
    0-49, F

score = int(input("Enter your score: "))
if score<=100 and score>=80:
    print("Your grade is A")
elif score<=79 and score>=70:
    print("Your grade is B")
elif score<=69 and score>=60:
    print("Your grade is C")
elif score<=59 and score>=50:
    print("Your grade is D")
elif score <= 0 and score >= 49:
    print("Your grade is F")
'''
'''
    Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter the month: ")
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autumn:
    print("This is autumn")
elif month in winter:
    print("This is winter")
elif month in spring:
    print("This is spring")
elif month in summer:
    print("This is summer")
'''
'''
    The following list contains some fruits:

    fruits = ['banana', 'orange', 'mango', 'lemon']

    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
my_fruit = input("Enter the fruit: ")
if my_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(my_fruit)
    print(fruits)
'''
'''
    Exercises: Level 3

    Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
  else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:

    Asabeneh Yetayeh lives in Finland. He is married.
'''
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
skills = person.get("skills")
print(skills)
front_end = {"JavaScript", "React"}
back_end = {"Node", "Python", "MongoDB"}
full_stack = {"React", "Node", "MongoDB"}

if skills is not None:
    middle_num = round(len(skills)/2)
    print(skills[middle_num])

    if "Python" in skills:
        print("He knows Python.")
    skills = set(skills)
    if front_end.difference(skills) is None:
        print('He is a front end developer')
    elif len(back_end.union(skills)) >= len(back_end):
        print('He is a backend developer')
    elif len(full_stack.union(skills)) >= len(full_stack):
        print('He is a fullstack developer')
    else:
        print('unknown title')
    if person.get("is_marred") == True and person.get("country") == "Finland":
        first_name = person.get("first_name")
        last_name = person.get("last_name")

        print(f"{first_name} {last_name} lives in Finland. He is married.")
