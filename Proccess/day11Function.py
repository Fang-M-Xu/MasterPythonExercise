import math
'''
Exercises: Day 11
Exercises: Level 1

    Declare a function add_two_numbers. It takes two parameters and it returns a sum.
    Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    Write a function called calculate_slope which return the slope of a linear equation
    Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

    Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

    Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050

    Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

Exercises: Level 2

    Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

    Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    Call your function is_empty, it takes a parameter and it checks if it is empty or not
    Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

Exercises: Level 3

    Write a function called is_prime, which checks if a number is prime.
    Write a functions which checks if all items are unique in the list.
    Write a function which checks if all the items of the list are of the same data type.
    Write a function which check if provided variable is a valid python variable
    Go to the data folder and access the countries-data.py file.

    Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''

def add_two_numbers(num1,num2):
    sum_num = num1 + num2
    return sum_num
print(add_two_numbers(2,3))

def area_of_circle(radius):
    area = math.pi * radius**2
    return area
print(area_of_circle(2))

def add_all_nums(*nums):
    sum_num = 0
    for num in nums:
        if type(num) == type(12):
            sum_num += num
    return sum_num
print(add_all_nums(2,3,4))

def convert_celsius_to_fahrenheit(celsius):
    fahr = (celsius * (9/5)) + 32
    return fahr
print(convert_celsius_to_fahrenheit(25))

def reverse_list(lst):
    lst = list(lst)
    len_lst = len(lst)
    reverse_lst=[]
    while  len_lst > 0:
        reverse_lst.append(lst[len_lst-1])
        len_lst -=1
    return reverse_lst

print(reverse_list([2,5,12,8]))

def remove_item(lst,keyw):
    lst = list(lst)
    lst.remove(keyw)
    return lst
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'],'Mango'))

def sum_of_numbers(par_num):
    sum_num=0
    for num in range(par_num+1):
        sum_num += num
    return sum_num
print(sum_of_numbers(10))

def sum_of_odds(par_num):
    sum_num = 0
    for num in range(par_num + 1):
        if num%2 != 0:
            sum_num += num
    return sum_num

print(sum_of_odds(10))

def evens_and_odds(par_num):
    num_evens = 0
    num_odds = 0
    for num in range(par_num + 1):
        if num%2 != 0:
            num_odds += 1
        if num%2 == 0:
            num_evens += 1
    print(f'The number of odds are {num_odds}.')
    print(f'The number of evens are {num_evens}.')
evens_and_odds(14)

def factorial(par_num):
    if (par_num == 0) or (par_num == 1):
        return 1
    else:
        return par_num*factorial(par_num-1)

print(factorial(5))

def calculate_mean(num_lst):
    num_lst = list(num_lst)
    mean = sum(num_lst).len(num_lst)
    return mean

def calculate_median(num_lst):
    num_lst = list(num_lst)
    num_lst.sort()
    middle_index = round(len(num_lst+1)/2)
    return num_lst[middle_index]

def calculate_mode(num_lst):
    num_lst = list(num_lst)
    dic_nums = {}
    for item in num_lst:
        if dic_nums.get(item) is not None:
            dic_nums[item]
    print(dic_nums)


def calculate_range(num_lst):
    num_lst = list(num_lst)
    num_lst.sort()
    return num_lst[-1]-num_lst[0]

def calculate_variance(num_lst):
    num_lst = list(num_lst)
    n = len(num_lst)
    mean = sum(num_lst) / n
    deviations = [(x - mean) ** 2 for x in num_lst]
    variance = sum(deviations) / n
    return variance

#(standard deviation)
def calculate_std(num_lst):
    num_lst = list(num_lst)
    var = calculate_variance(num_lst)
    std_dev = math.sqrt(var)

    return std_dev




