#Day2:30 days of python programming
import math

first_name, last_name, full_name = "Jack", "White", "J.White"
country = "USA"
city = "New York"
age = 25
year = 2021
is_married = False
is_true = True
is_light_on = False

print(type(first_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))


num_one =5
num_two = 4
total = num_one+num_two
diff = num_one - num_two
product = num_one*num_two
division = num_one/num_two
remaider = num_two%num_one
exp = pow(num_one,num_two)
floor_division = num_one//num_two

print('total: ',total,', diff: ',diff,', product: ',product,', division: ',division,', remaider: ',remaider,', exp: ',exp,', floor_division: ',floor_division)

r = float(input("PLease set the radius: "))
area_of_circle = math.pi * r * r
circum_of_circle = math.pi * r * 2
print('area_of_circle: ',area_of_circle, ', circum_of_circle: ', circum_of_circle)

first_name = input("PLease enter first name: ")
last_name = input("PLease enter last name: ")
country = input("PLease enter country: ")
age = input("PLease enter age: ")

print("Your info:", first_name,last_name,country,age)

# help("input")






