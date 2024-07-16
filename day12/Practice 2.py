def print_show_info(tv_show):
    title = tv_show.get("title")
    seasons = tv_show.get("seasons")
    initial_release = tv_show.get("initial_release")
    print(f"{title} ({initial_release}) - {seasons} seasons")
