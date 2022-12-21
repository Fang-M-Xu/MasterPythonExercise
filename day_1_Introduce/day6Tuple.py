import math
'''
Exercises: Level 1

    Create an empty tuple
    Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
    Join brothers and sisters tuples and assign it to siblings
    How many siblings do you have?
    Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Exercises: Level 2
    Unpack siblings and parents from family_members
    Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
    Change the about food_stuff_tp tuple to a food_stuff_lt list
    Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
    Slice out the first three items and the last three items from food_staff_lt list
    Delete the food_staff_tp tuple completely
    Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''

tuple_test = tuple()
tuple_brothers = ('Jack','Harry','Tom','Frank')
tuple_sisters = ('Lucy','Mary','Lily')
tuple_siblings = tuple_brothers+tuple_sisters
print(tuple_siblings, len(tuple_siblings))
tuple_siblings = list(tuple_siblings)
tuple_siblings.append('Horry')
tuple_siblings.append('Jan')
family_members = tuple(tuple_siblings)
print(family_members)

tuple_siblings_new = family_members[-len(family_members):-2]
print(tuple_siblings_new)
tuple_parents = family_members[-2::]
print(tuple_parents)

fruits=('Apple','Orange','Banana')
vegetables=('Eggfruit','Cumcomber','Potato','Tomato')
animal=('Cat','Dog','Tiger')

food_stuff_tp = fruits+vegetables+animal
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
middle_num = math.ceil((len(food_stuff_lt)-1)/2)
print(middle_num)
middle_item = food_stuff_lt[middle_num]
print(middle_item, food_stuff_lt[0:3],food_stuff_lt[-3::])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)