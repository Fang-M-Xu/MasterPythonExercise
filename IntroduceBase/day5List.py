import math

'''
Exercises: Level 1

    Declare an empty list
    Declare a list with more than 5 items
    Find the length of your list
    Get the first item, the middle item and the last item of the list
    Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
    Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
    Print the list using print()
    Print the number of companies in the list
    Print the first, middle and last company
    Print the list after modifying one of the companies
    Add an IT company to it_companies
Insert an IT company in the middle of the companies list
Change one of the it_companies names to uppercase (IBM excluded!)
 Join the it_companies with a string '#;  '
  Check if a certain company exists in the it_companies list.
  Sort the list using sort() method
  Reverse the list in descending order using reverse() method
  Slice out the first 3 companies from the list
Slice out the last 3 companies from the list
Slice out the middle IT company or companies from the list
Remove the first IT company from the list
Remove the middle IT company or companies from the list
Remove the last IT company from the list
Remove all IT companies from the list
Destroy the IT companies list

'''
first_list = list()
second_list = [0,2,4,1,6]
print(len(first_list), len(second_list))

print(second_list[0], second_list[len(second_list)-1],second_list[round((len(second_list)-1)/2)])
mixed_data_types=['Jack', 22, 173.29, False, 'Jerusalem']
print(mixed_data_types)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies, len(it_companies))
print(it_companies[0], it_companies[len(it_companies)-1],it_companies[round((len(it_companies)-1)/2)])
it_companies[0] = 'Tiwtter'
print(it_companies)
it_companies.append('Alibaba')
it_companies.insert(round((len(it_companies)-1)/2), 'DD')
it_companies[2].upper()
it_companies_str = '#;  '.join(it_companies)
print(it_companies_str)
print('QWE' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[0:3],'：：：：',it_companies[-3:-2])
middele_num = (len(it_companies)-1)/2
print(middele_num, math.floor(middele_num), math.ceil(middele_num), it_companies[math.floor(middele_num):math.ceil(middele_num)+1])
it_companies.pop(0)
print(it_companies)
it_companies.pop(round(middele_num))
print(it_companies)
it_companies.pop(-1)
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

'''
    Join the following lists:

    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)
full_stack = new_list.copy()
print(full_stack)
full_stack.insert(full_stack.index('Redux')+1,['Python','SQL'])
print(new_list,'\n',full_stack)

'''
Exercises: Level 2

    The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    Sort the list and find the min and max age
    Add the min age and the max age again to the list
    Find the median age (one middle item or two middle items divided by two)
    Find the average age (sum of all items divided by their number )
    Find the range of the ages (max minus min)
    Compare the value of (min - average) and (max - average), use abs() method

    Find the middle country(ies) in the countries list
    Divide the countries list into two equal lists if it is even if not one more country for the first half.
    ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''
print('ages====================')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sort_ages = sorted(ages)
print(sort_ages, sort_ages[0], sort_ages[-1])
new_list = list()
new_list.append(sort_ages[0])
new_list.append(sort_ages[-1])
print(new_list)
middle_ages = (len(sort_ages)-1)/2
print(sort_ages[math.ceil(middle_ages)])
average = sum(sort_ages)/len(sort_ages)
print(sum(sort_ages), 'average: ',average)
print('range: ', sort_ages[-1]-sort_ages[0])
min = abs(sort_ages[0] - average)
max = abs(sort_ages[-1] - average)
print('compare: ', min <= max)

countries =  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_item, second_item, third_item, *rest = countries
print(first_item, second_item, third_item, rest)