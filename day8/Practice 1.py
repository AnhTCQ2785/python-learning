import random
number_to_guess = random.randint(1, 100)
guessed_correctly = False
print("Welcome to the guessing game! Try to guess the number between 1 and 100.")

while not guessed_correctly:
    guess = int(input("Enter your guess: "))

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        guessed_correctly = True