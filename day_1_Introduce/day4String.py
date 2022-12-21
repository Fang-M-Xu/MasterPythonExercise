'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''
mul_string = ['Thirty', 'Days', 'Of', 'Python']
single_string = ' '.join(mul_string)
print(single_string)

'''
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''
mul2_string = ['Coding', 'For' , 'All']
sin2_string = ' '.join(mul2_string)
print(sin2_string)

'''
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
'''
company = 'Coding For All'
print(company, len(company), company.upper(), company.lower())
print(company.capitalize(), company.title(), company.swapcase())
print(company.split()[0])
sub_sting = 'Coding'
print(company.find(sub_sting))
new_str = company.replace('Coding',"Python")
print(new_str)
every_str = new_str.replace('All',"Everyone")
print(every_str)
print(company.split(' '))
last_index = len(company) - 1
print(company[0], last_index, company[10])
pfe_list = every_str.split()
acronym_every = pfe_list[0][0] +  pfe_list[1][0] +  pfe_list[2][0]
print(acronym_every)
cfa_list = company.split()
acronym_coding = cfa_list[0][0] +  cfa_list[1][0] +  cfa_list[2][0]
print(acronym_coding)
print(company.find('C'), company.find('F'), company.rfind('l'))
print(company.startswith('Coding'), company.endswith('coding'))

'''
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''
brand = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(brand.split(','))
sta1= 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction')
print(sta1.find('because'), sta1.rindex('because'))
print(sta1.find('because'), sta1.rfind('because'))
print(sta1.strip('because because because'), sta1.find('because'))
'''
Which one of the following variables return True when we use the method isidentifier():

    30DaysOfPython
    thirty_days_of_python

The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
'''
#2

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(lib))
'''
    Use the new line escape sequence to separate the following sentences.

    I am enjoying this challenge.
    I just wonder what is next.

    Use a tab escape sequence to write the following lines.

    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki

    Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

    Make the following using string formatting methods:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
print('I am enjoying this challenge.\n I just wonder what is next.')
print('Name \tAge\tCountry\tCity')
print('Asabeneh \t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

a,b = 8, 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')










