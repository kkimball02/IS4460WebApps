import requests
import json

new_movie_data = {'title': 'Shreck 3', 'description': "It's the year 3000 A.D., and the Earth is lost to the alien race of Psychlos. Humanity is enslaved by these gold-thirsty tyrants, who are unaware that their 'man-animals' are about to ignite the rebellion of a lifetime.", 'director': 'Roger Christian', 'release_year': '2000', 'budget': '$44 million', 'runtime':'1h 59m', 'rating': 'PG-13', 'genre':'Sci-Fi' }

response = requests.post('http://localhost:8000/api/movies/', data=json.dumps(new_movie_data), headers={'Content-Type': 'application/json'})
print(response.json())


