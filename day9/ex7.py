movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)

for title, director in movies:
    print(f"{title} by {director}.")

movies_list = list(movies)

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")
