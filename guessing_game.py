#This is a python game that generates a random number using the random library and then asks the user for an input and if the user guesses correct he is notified!
#Game by Charles U.

import random

def guessing_game (x):
    #x is the maximum limit of the guess.
    random_number = random.randint(1, x)
    user_guess = 0
    while(user_guess != random_number):
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < random_number:
            print("Not correct, too low!")
            
        elif user_guess > random_number:
            print("Not correct, too high!")
    print(f"You guessed {user_guess} correctly!")

max_guess = int(input("Enter max number allowed: "))
guessing_game(max_guess)
