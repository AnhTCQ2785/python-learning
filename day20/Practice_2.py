names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

filtered_names = [name.title() for name in names if len(name) < 8]

print(filtered_names)
