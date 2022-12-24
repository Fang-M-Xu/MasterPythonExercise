import requests,json
from bs4 import BeautifulSoup

url = "http://www.bu.edu/president/boston-university-facts-stats"

# response = requests.get(url)
# content = response.content
# soup = BeautifulSoup(content,'html.parser')
#
# print(soup.title.get_text())
# print(soup.body)

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

with open('./data/person.json','w') as f:
    json.dump(person, f)
