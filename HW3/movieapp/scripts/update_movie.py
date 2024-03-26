import requests
import json

movie_id = 2

updated_data = {'title': 'Shreck 3', 'release_year': '2007'}
response = requests.put(f'http://localhost:8000/api/movies/{movie_id}/', data=json.dumps(updated_data), headers={'Content-Type': 'application/json'})
print(response.json())
