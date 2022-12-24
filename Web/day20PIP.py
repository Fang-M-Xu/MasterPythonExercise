import numpy,requests

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(type(np_arr))

'''
Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
'''
respones = requests.get(url='http://www.gutenberg.org/files/1112/1112.txt')

list_content = respones.text.split()
dict_word={}
for word in list_content:
    if dict_word.get(word) == None:
        dict_word[word] = 1
    else:
        dict_word[word] += 1
sort_words = sorted(dict_word.items(),reverse=True,key = lambda x:x[1])
print(sort_words[0:10])
