def read_file():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError as e:
        print("Error: File not found.", e)

read_file()
read_file()
import os
