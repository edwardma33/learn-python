import os
def clear():
    os.system("clear")
import game_data
data = game_data.data
import random
print(len(data))
print("Welcome to the Higher Lower Game!")
print("Goal:\n Guess which pick has more followers\n ")

score = 0

while input("Would you like to play? [y/n]: ") == "y":
    if score != 0:
        person_1 = data[random.randint(0, len(data) - 1)]
    else:
        person_1 = data[random.randint(0, len(data) - 1)]
    person_2 = data[random.randint(0, len(data) - 2)]

    if 

    while 