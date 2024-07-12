# Step 1: Convert tuple to dictionary
album_tuple = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)

album_dict = {
    "album_name": album_tuple[0],
    "artist": album_tuple[1],
    "year_of_release": album_tuple[2],
    "track_list": album_tuple[3]
}

# Step 2: Iterate over dictionary keys and values
for key, value in album_dict.items():
    print(f"{key}: {value}")

# Step 3: Delete keys and add date_of_release
del album_dict["track_list"]
del album_dict["year_of_release"]

album_dict["date_of_release"] = "March 1st, 1973"

# Step 4: Try to retrieve a deleted value and handle the KeyError
try:
    print(album_dict["year_of_release"])
except KeyError as e:
    print(f"KeyError: {e}")


year_of_release = album_dict.get("year_of_release")
print(f"Year of Release (using get): {year_of_release}")
