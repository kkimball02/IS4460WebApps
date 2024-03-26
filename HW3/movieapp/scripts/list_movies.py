import requests
import json

response = requests.get('http://127.0.0.1:8000/api/movies/')
print(response.text)
print(response.headers)