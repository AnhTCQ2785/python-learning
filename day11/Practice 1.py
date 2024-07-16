empty_set = set()

empty_set.add("apple")
empty_set.add("banana")
empty_set.add("orange")

second_set = {"banana", "grape", "pineapple"}

union_set = empty_set.union(second_set)
print("Union:", union_set)

sym_diff_set = empty_set.symmetric_difference(second_set)
print("Symmetric Difference:", sym_diff_set)

intersection_set = empty_set.intersection(second_set)
print("Intersection:", intersection_set)

numbers_range = range(1, 11)
user_number = int(input("Enter a number: "))

if user_number in numbers_range:
    print(f"{user_number} is within the range of {numbers_range}")
else:
    print(f"{user_number} is not within the range of {numbers_range}")
