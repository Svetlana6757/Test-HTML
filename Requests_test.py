'''
import requests
import pprint
response = requests.get('https://www.google.com')
print(response.status_code)
if response.ok:
    print('запрос успешно обработан')
else:
    print('произошла ошибка')

print(response.content)

response = requests.get('https://api.github.com')
print(response.text)
response_json = response.json()
pprint.pprint(response_json)'''

'''
import requests
import pprint
params = {
    'q': 'JavaScript'
}

response = requests.get(url='https://api.github.com/search/repositories', params=params)

response_json = response.json()
pprint.pprint(response_json)

print(f"Количество репозиториев с js: {response_json['total_count']}")'''


import requests

img = "https://natalyland.ru/wp-content/uploads/1/6/5/165a740577042cbe692c33af365d14d1.jpeg"
response = requests.get(img)

with open('test.jpg', 'wb') as file:
   file.write(response.content)