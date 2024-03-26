import requests
import json

movie_id = 3
response = requests.delete(f'http://localhost:8000/api/movies/{movie_id}/')
print(response.status_code)
