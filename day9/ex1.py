movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for index in range(len(movies)):
    print(f"{index + 1}. {movies[index][0]} ({movies[index][2]}), by {movies[index][1]}")
