import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework_2.settings')

django.setup()
from movie_app.models import Movie, User

##for loops to delete records
movies = Movie.objects.all()
for movie in movies:
    movie.delete()

users = User.objects.all()
for user in users:
    user.delete()

#Instantiating
movies_data = [{"title":"The Godfather", "description":"The Godfather. Best-written, best-acted, most beautiful film about the immigrant experience ever contemplated. It invented most modern clichés.", "director":"Francis Ford Coppola", "release_year": "1972", "budget": "$6-7 million", "runtime": "2h 55m", "rating": "R", "genre": "drama"},
               {"title":"The Dark Knight", "description":"With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.",
                "director":"Christopher Nolan", "release_year": "2008", "budget": "$185 million", "runtime": "2h 12m", "rating": "PG-13", "genre": "action"},
                {"title":"The Shawshank Redemption", "description":"Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.", "director":"Frank Darabont", "release_year": "1994", "budget": "$25 million", "runtime": "2h 22m", "rating": "R", "genre": "drama"},
                {"title":"Forrest Gump", "description": "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.", "director":"Robert Zemeckis", "release_year": "1994", "budget": "$55 million", "runtime": "2h 22m", "rating": "PG-13", "genre": "drama"},
                {"title":"Star Wars: Episode IV - A New Hope", "description": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.", "director":"George Lucas", "release_year": "1977", "budget": "$11 Million", "runtime": "2h 1m", "rating": "PG", "genre": "action"},
                {"title":"E.T. the Extra-Terrestrial", "description":"A troubled child summons the courage to help a friendly alien escape from Earth and return to his home planet.", "director":"Steven Speilberg", "release_year": "1982", "budget": "$10.5 million", "runtime": "1h 55m", "rating": "PG", "genre": "adventure"},
                {"title":"The Silence of the Lambs", "description":"A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.", "director":"Jonathan Demme", "release_year": "1991", "budget": "$19 million", "runtime": "1h 58m", "rating": "R", "genre": "crime"},
                {"title":"Saving Private Ryan", "description":"Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.", "director":"Steven Speilberg", "release_year": "1998", "budget": "$65–$70 million", "runtime": "2h 49m", "rating": "R", "genre": "drama"},
                {"title":"Jaws", "description":"When a killer shark unleashes chaos on a beach community off Cape Cod, it's up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.", "director":"Steven Speilberg", "release_year": "1975", "budget": "$9 million", "runtime": "2h 10m", "rating": "PG", "genre": "adventure"},
                {"title":"Jurassic Park", "description":"A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.", "director":"Steven Speilberg", "release_year": "1993", "budget": "$63 million", "runtime": "2h 7m", "rating": "PG-13", "genre": "action"}]
for movie_data in movies_data:
    movie = Movie(**movie_data)
    movie.save()

user_data = [{"username": "kkimball20", "password":"Il!ked0gs", "first_name": "Kyler", "last_name":"Kimball", "email": "kyler.kimball123@gmail.com" },
             {"username": "john_doe", "password":"pass123", "first_name":"John", "last_name": "Doe", "email":"johndoe@gmail.com"},
             {"username": "jane_smith", "password":"abc456", "first_name": "Jane", "last_name":"Smith", "email":"jane_smith@gmail.com"}] 

for users_data in user_data:
    user = User(**users_data)
    user.save()

##queries
all_movies = Movie.objects.get(all)
print(all_movies)





movies_starting_with_text = Movie.objects.filter(title__startswith=("S"))

print(movies_starting_with_text)
#To view or search for the movies
print(movies_starting_with_text[1].title)

one_movie = Movie.objects.get(pk = 3)
##To view change
print(one_movie.title)

update_movie = Movie.objects.get(pk=2)
update_movie.genre = 'crime'
update_movie.save()
##To view the change
print(Movie.objects.get(pk = 2).genre)

delete_movie = Movie.objects.get(pk=1)
delete_movie.delete()
print(delete_movie.title)
delete_movie.save()

##Getting user data by supplying a username
username = 'kkimball20'
user_data = User.objects.get(username = username)
print(user_data.username)
print(user_data.password)
print(user_data.email)












