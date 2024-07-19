def add(a, b):
    result = a + b
    print(f"The result of adding {a} and {b} is {result}")


def subtract(a, b):
    result = a - b
    print(f"The result of subtracting {b} from {a} is {result}")


def multiply(a, b):
    result = a * b
    print(f"The result of multiplying {a} and {b} is {result}")


def divide(a, b):
    if b == 0:
        print("Warning: Division by zero is not allowed.")
    else:
        result = a / b
        print(f"The result of dividing {a} by {b} is {result}")
