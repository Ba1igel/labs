# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# First task
def s_above(movie):
    return movie["imdb"] > 5.5

def sublist(moviess):
    return[movie for movie in moviess if s_above(movie)]

def in_category(moviess, category):
    return[movie for movie in moviess if movie["category"] == category]

def average_imdb(moviess):
    if not moviess:
        return 0; 
    total_s = sum(movie["imdb"] for movie in moviess)
    return total_s / len(moviess)

def average_imdb_score(moviess, category):
    category_movies = in_category(moviess, category)
    return average_imdb(category_movies)

print(s_above(movies[0]))
print(sublist(movies))
print(in_category(movies, "Drama"))
print(average_imdb(movies))
print(average_imdb_score(movies, "Drama"))