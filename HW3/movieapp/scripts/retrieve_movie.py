import requests
import json

movie_id = 1  


response = requests.get(f'http://localhost:8000/api/movies/{movie_id}/')
print(response.json())

