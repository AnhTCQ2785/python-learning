'''# names = ["John", "Alice", "Sarah", "George"]
# print(names)
#movie_titles = [
#    "Eternal Sunshine of the Spotless Mind",
#   "Memento",
#  "Requiem for a Dream"
#]

#friend_details = ["John", 27, "Web Developer"]

#print(friend_details)

names = ["John", "Alice", "Sarah", "George"]

print(names[2])  # Sarah

names = ["John", "Alice", "Sarah", "George"]
names.append("Simon")

print(names[-1])  # Simon


names = ["John", "Alice", "Sarah", "George"]
names =  ["Simon"]+ names
print(names)  # Simon

numbers = [1, 2, 4, 5]
numbers.insert(2, 3)

print(numbers)  # [1, 2, 3, 4, 5]

names = ["John", "Sarah", "Alice", "John"]
names.remove("John")

print(names)  # ['Sarah', 'Alice', 'John']

names = ["John", "Sarah", "Alice", "Mike"]
del names[2]

print(names)  # ['Sarah', 'Alice', 'Mike']
names = ["John", "Sarah", "Alice", "Mike"]
last_in_line = names.pop()

print(names)         # ['John', 'Sarah', 'Alice']
print(last_in_line)  # Mike

names = ["John", "Sarah", "Alice", "John"]
names.clear()

print(names)  # []

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
print(movies)
'''
movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]
print(movies[0])
