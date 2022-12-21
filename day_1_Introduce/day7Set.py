import math

'''
Exercises: Level 1

    Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies
    What is the difference between remove and discard

Exercises: Level 2

    Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B
    Delete the sets completely

Exercises: Level 3

    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    Explain the difference between the following data types: string, list, tuple and set
    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
new_IT = {'Alibaba','DD','Baidu'}
it_companies.update(new_IT)
print(it_companies)
it_companies.pop()
print(it_companies)
print("============")
C = A.union(B)
print(C)
D = A.intersection(B)
print(D)
print(type(D))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del D

age_set = set(age)
print(len(age_set)>=len(age))

sente = 'I am a teacher and I love to inspire and teach people.'
sente_lt = sente.split(" ")
print(sente_lt)
sente_set = set(sente_lt)
print(sente_set)