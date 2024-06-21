"""
list: []
index: 0
"""
#          0 1 2 - index/position
numbers = [1, 2, 3]  # - value
print(type(numbers))
print(len(numbers))

print(numbers[0])

"""
list

"""
length = len(numbers)
print(numbers[length - 1])

# change value
numbers[1] = 1000
print(numbers)
numbers[2] = 'a'
print(numbers)

numbers[-3] = 'c'
print(numbers)

numbers[2] = 10000
print(numbers)
