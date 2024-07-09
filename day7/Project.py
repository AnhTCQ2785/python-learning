movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron",365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
total_budget = sum(budget for _, budget in movies)
average_budget = total_budget / len(movies)

higher_than_average_movies = [(title, budget - average_budget) for title, budget in movies if budget > average_budget]
count_higher_than_average = len(higher_than_average_movies)

print(f"Average budget: ${average_budget:.2f}")

for title, excess_budget in higher_than_average_movies:
    print(f"{title} spent ${excess_budget:.2f} more than the average budget")

    print(f"Number of movies that spent more than the average budget: {count_higher_than_average}")