
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
match_lst = [i for i in numbers if i<=0]
print(match_lst)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [numb for row1 in list_of_lists for row2 in row1 for numb in row2]
print(flattened_list)

numbers_pair = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(numbers_pair)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [country for row1 in countries for row2 in row1 for country in row2]
print(new_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country':info[0],'city':info[1]} for row in countries for info in row]
print(dict_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
con_names = [name[0]+' '+name[1] for row in names for name in row]
print(con_names)