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
pprint.pprint(response_json)
pprint.pprint(response_json)'''

import requests

params = {
    'q': 'html'
}

response = requests.get(url='https://api.github.com/search/repositories', params=params)

response_json = response.json()

print(response.status_code)
print(f"Количество репозиториев с html: {response_json['total_count']}")

