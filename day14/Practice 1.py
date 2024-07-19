with open("hello_world.txt", "w") as f:
    f.write("Hello, World!")
    f.write("\nHow are you?")
import csv
data = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
]

with open("iris_data.csv", "w", newline='') as file:
    for dat in data:
        result = str(dat) + '\n'
        file.write(result)



