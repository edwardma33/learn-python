import os
def clear():
    os.system("clear")
import game_data
data = game_data.data
import random

clear()
print("Welcome to the Higher Lower Game!")
print("Goal:\n Guess which pick has more followers\n ")

score = 0
answer = 999 
prev_winner = ""

while score >=0 and (score > 0 or input("Would you like to play? [y/n]: ") == "y"):
    if score != 0:
        person_1 = data[data.index(prev_winner)]
    else:
        person_1 = data[random.randint(0, len(data) - 1)]
        clear()
    person_2 = data[random.randint(0, len(data) - 2)]

    if person_1['follower_count'] > person_2['follower_count']:
        prev_winner = person_1
        answer = person_1['name']
        more_follows = person_1['follower_count']
        less_follows = person_2['follower_count']
        other = person_2['name']
    else:
        prev_winner = person_2
        answer = person_2['name']
        more_follows = person_2['follower_count']
        less_follows = person_2['follower_count']
        other = person_1['name']

    print(f"{person_1['name']} is a {person_1['description']} from {person_1['country']}\n")
    print(f"{person_2['name']} is a {person_2['description']} from {person_2['country']}\n")

    guess = input(f"Who has more followers on insta?: [{person_1['name']}, {person_2['name']}]: ")
    while guess != person_1['name'] and guess != person_2['name']:
        guess = input(f"Who has more followers on insta?: [{person_1['name']}, {person_2['name']}]: ")
    clear()

    if guess == answer:
        score += 1
        print(f"The answer is {answer}...\n \n{answer} has {more_follows} million followers and {other} has {less_follows} million followers.")
        print(f"Score: {score}")
    elif score == 50:
        score = -1
        print("YOU BEAT THE GAME!!!")
    else:
        print("Game over...")
        print(f"The answer was {answer}...\n \n{answer} has {more_follows} million followers and {other} has {less_follows} million followers.")
        print(f"Your score was: {score}")
        score = -1
