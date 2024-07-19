def add(a, b):
    print(f"The result of adding {a} and {b} is {a + b}")


def subtract(a, b):
    print(f"The result of subtracting {b} from {a} is {a-b}")


def multiply(a, b):
    print(f"The result of multiplying {a} and {b} is {a * b}")


def divide(a, b):
    if b == 0:
        print("Warning: Division by zero is not allowed.")
    else:
        print(f"The result of dividing {a} by {b} is {a / b}")


add(3, 4)
subtract(6, 5)
multiply(7, 8)
divide(8, 4)
