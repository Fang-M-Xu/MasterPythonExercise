
'''
Write a function which count number of lines and number of words in a text.
All the files are in the data the folder:
a) Read obama_speech.txt file and count number of lines and words
b) Read michelle_obama_speech.txt file and count number of lines and words
c) Read donald_speech.txt file and count number of lines and words
d) Read melina_trump_speech.txt file and count number of lines and words
'''
import csv
import json
from data.stop_words import stop_words
'''
# obama_speech.txt
with open("./data/romeo_and_juliet.txt") as f:
    dict_obama_speech_num = {}
    obama_speech = f.read().splitlines()
    # print(obama_speech)
    # print("Number of lines: ",len(obama_speech))
    count_words = 0
    for sen in obama_speech:
        sentence = sen.split()
        count_words += len(sentence)
        for item in sentence:
            if item.lower() in stop_words:
                continue
            if dict_obama_speech_num.get(item) == None:
                dict_obama_speech_num[item] = 1
            else:
                dict_obama_speech_num[item] = dict_obama_speech_num[item] + 1
    rev_obama_speech_num = sorted(dict_obama_speech_num.items(),reverse=True,key=lambda x:x[1])
    print(rev_obama_speech_num[0:10])
    print("Number of words: ",count_words)

print("Donald speech")

with open("./data/donald_speech.txt") as f:
    donald_speech = f.read().splitlines()
    print(donald_speech)
    print("Number of lines: ",len(donald_speech))
    count_words = 0
    for sen in donald_speech:
        sentence = sen.split()
        count_words += len(sentence)
    print("Number of words: ",count_words)

with open('./data/melina_trump_speech.txt') as f:
    melina_trump_speech = f.read().splitlines()
    print(melina_trump_speech,len(melina_trump_speech))
'''

def most_spoken_languages(filename,number):
    dict_name={}
    with open(filename) as f:
        countries_name = json.load(f)
    # print(countries_name)
    for item in countries_name:
        languages = item['languages']
        for language in languages:
            if dict_name.get(language) == None:
                dict_name[language] = 1
            else:
                dict_name[language] = dict_name[language]+1
    rev_name_sort = sorted(dict_name.items(),reverse=True,key=lambda x:x[1])
    print(rev_name_sort[0:number])
# most_spoken_languages("./data/countries_data.json",3)


def most_populated_countries(filename,number):
    populated_countries = {}
    with open(filename) as f:
        data_country = json.load(f)
    for item in data_country:
        populated_countries[item['name']]=item['population']
    sort_populated_countries = sorted(populated_countries.items(),reverse=True,key= lambda x:x[1])

    list_populated_countries =[]
    for item in sort_populated_countries[0:number]:
        dict_populated_countries={}
        dict_populated_countries["country"] = item[0]
        dict_populated_countries["population"] = item[1]
        list_populated_countries.append(dict_populated_countries)
    print(list_populated_countries)

# most_populated_countries("./data/countries_data.json",10)

'''
Read the hacker news csv file and find out: 
a) Count the number of lines containing python or Python 
b) Count the number lines containing JavaScript, javascript or Javascript 
c) Count the number lines containing Java and not JavaScript
'''
import csv
with open('./data/hacker_news.csv') as f:
    hacker_news = csv.reader(f,delimiter=',')
    count=0
    for row in hacker_news:
        if ('python' in row[1]) or ('Python' in row[1]):
            count +=1
            print(row[1])
    print(count)