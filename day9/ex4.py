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

for counter, movie in enumerate(movies, start=1):      '''tạo ra một cặp giá trị gồm counter (số thứ tự của phim bắt đầu từ 1) và movie (tuple chứa thông tin về phim).'''
    print(f"{counter}. {movie[0]} ({movie[2]}), by {movie[1]}")
