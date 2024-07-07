'''''
numbers = [1, 2, 3, 4, 5]
numbers = str(numbers)
print(numbers)
''
project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {project_authors}.")


user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
numbers_list = user_numbers.split(",")

print(numbers_list) # ['1', ' 2', ' 3', ' 4', ' 5']

name=input("Please enter ur current name: ")
name_list = name.split(",")
print(name_list)
'''''

