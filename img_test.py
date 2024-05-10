
import requests

img = "https://natalyland.ru/wp-content/uploads/1/6/5/165a740577042cbe692c33af365d14d1.jpeg"
response = requests.get(img)

with open('test.jpg', 'wb') as file:
   file.write(response.content)