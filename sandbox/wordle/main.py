import os
import random

words = ["about", "above", "hello", "world"]

def pick_word():
    return words[random.randint(0, len(words) - 1)] 


picked_word = pick_word()
picked_word = [*picked_word]
print(picked_word)

while input("Would you like to play?: [y/n]; ") == "y":
    