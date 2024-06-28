movies = [
    ('Taxi drivers', 'Director: Martin Scorsese', 1976, 'Budget: Approximately 1.9 million USD'),
    ('Black Home', ' Director: Shin Tae-ra', 1999, 'Budget: 1 milion USD')
]

title = input('Enter the title of the movie: ')
director = input('Enter the director name of the movie: ')
budget = input('Enter the budget of the movie: ')
released_year = int(input('Enter the release year of the movie: '))  # Convert input to integer

new_movie = (title, director, released_year, budget)

print(f"The movie '{new_movie[0]}' was released in {new_movie[2]}.")

movies.append(new_movie)

print("List of films: ")    
for movie in movies:
    print(movie)
print("List of films after update:")
for movie in movies:
    print(movie)
