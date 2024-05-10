import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': "Заголовок или название созданного объекта post запроса",
    'foo': "Краткое описание post запроса",
    'bar': "Контент post запроса",
    'body': "Основное содержимое post запроса",
    'userID': 1
}

response = requests.post(url, data=data)
print(response.status_code)
print(f'ответ - {response.json()}')