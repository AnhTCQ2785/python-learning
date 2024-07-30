import random as rnd

def guessing_game():
    number_to_guess = rnd.randint(1, 100)
    guess = None
    
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
guessing_game()
