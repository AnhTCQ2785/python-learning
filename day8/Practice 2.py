string = "Python"
index = 0

while index < len(string):
    char = string[index]
    if char == 'o':
        index += 1
        continue
    print(char)
    index += 1
