import os
import random

def clear():
    os.system("clear")

print("Welcome to the number guessing game!")

while input("Would you like to play? [y/n]: ") == "y":
    if input("Choose a difficulty! [easy/hard]: ") == "easy":
        attempts = 10
    else:
        attempts = 5    
    answer = random.randint(0, 101)
    guess = 999
    clear()
    while attempts > 0 and guess != answer:
        guess = int(input("Pick a number between 1 and 100!: "))

        if guess == answer:
            print(f"You win!\nThe answer was {answer}")
        elif guess > answer:
            attempts -= 1
            if attempts == 0:
                print(f"Game over...\nThe number was {answer}")
            else:
              print(f"Too high\nAttempts left: {attempts}")
        else:
            attempts -= 1
            if attempts == 0:
                print(f"Game over...\nThe number was {answer}")
            else:
              print(f"Too low\nAttempts left: {attempts}")
clear()