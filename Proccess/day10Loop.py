from Files.countries import countries

'''
Exercises: Level 1

    Iterate 0 to 10 using for loop, do the same using while loop.

    Iterate 10 to 0 using for loop, do the same using while loop.

    Write a loop that makes seven calls to print(), so we get on the output the following triangle:

      #
      ##
      ###
      ####
      #####
      ######
      #######

    Use nested loops to create the following:

    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #

    Print the following pattern:

    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100

    Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

    Use for loop to iterate from 0 to 100 and print only even numbers

    Use for loop to iterate from 0 to 100 and print only odd numbers

Exercises: Level 2

    Use for loop to iterate from 0 to 100 and print the sum of all numbers.

The sum of all numbers is 5050.

    Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    The sum of all evens is 2550. And the sum of all odds is 2500.

Exercises: Level 3

    Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    X Go to the data folder and use the countries_data.py file.
        What are the total number of languages in the data
        Find the ten most spoken languages from the data
        Find the 10 most populated countries in the world

'''
count = 0
while count <= 10:
    print(count)
    count = count + 1
print("================================")
for i in range(11):
    print(i)
print("==============2==================")
acount = 10
while acount >= 0:
    print(acount)
    acount = acount -1
print("================================")
lst = list(range(11))
lst.reverse()
for i in lst:
    print(i)


for i in range(7):
    for j in range(i+1):
        print("#", end = ' ')
    print("")

for i in range(8):
    for j in range(8):
        print("#", end = ' ')
    print("")

for i in range(11):
    print(f'{i} * {i} = ', i*i)

skills =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in skills:
    print(item,end = ' ')
print("")

for i in range(101):
    if i%2 == 0:
        print(i, end = ' ')
print("")

for i in range(101):
    if i%2 != 0:
        print(i, end = ' ')
print("")

sum_num = 0
for i in range(101):
    sum_num += i
print("The sum of all numbers is ", sum_num)

sum_even = 0
sum_odd = 0
for i in range(101):
    if i%2 == 0:
        sum_even = sum_even + i
    if i%2 != 0:
        sum_odd = sum_odd + i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

land_countries = []
for item in countries:
    if 'land' in item:
        land_countries.append(item)
print(land_countries)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
# new_list = list()
# for item in fruits:
#     new_list.append(item)
