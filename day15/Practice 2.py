movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

title_case_movie = {key: value.title() for key, value in movie.items()}
print(title_case_movie)