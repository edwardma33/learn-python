import random
import os

def clear():
    os.system("clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
player_chips = 1000

dealer = []

while player_chips > 0 and input("Would you like to play a game? [y/n]: ") == "y":
    clear()
    bet = int(input(f"Current balance: {player_chips}\nHow much would you like to bet?: "))
    if bet > player_chips:
        bet = player_chips
    player.append(cards[random.randint(0, len(cards) - 1)])
    player.append(cards[random.randint(0, len(cards) - 1)])
    dealer.append(cards[random.randint(0, len(cards) - 1)])

    print(f"Your hand: {player}")
    print(f"Dealer hand: {dealer}")

    while sum(player) < 21 and input("[hit/stay]: ") == "hit":
        player.append(cards[random.randint(0, len(cards) - 1)])
        print(f"Your hand: {player}")
        print(f"Dealer hand: {dealer}")
        
    
    while sum(dealer) < 17 and sum(dealer) < 21 and sum(player) <= 21:
        dealer.append(cards[random.randint(0, len(cards) - 1)])
        print(f"Your hand: {player}")
        print(f"Dealer hand: {dealer}")
    
    player = sum(player)
    dealer = sum(dealer)

    if player > 21:
        print("BUST! Dealer win.")
        player_chips -= bet
    elif dealer > 21:
        print("Dealer bust! You win!")
        player_chips += bet
    elif player > dealer:
        print("You win!")
        player_chips += bet
    elif player == dealer:
        print("Draw.")
    else:
        print("Dealer Win.")
        player_chips -= bet
    
    print(f"|------Total------|\n|Player:      {player}  |\n|Dealer:      {dealer}  |\n|-----------------|\n|Chips:     {player_chips}  |")
    
    player = []
    dealer = []

clear()

if player_chips == 0:
    print("You lost everything!")
    print(f"Final balance: {player_chips}")
elif player_chips < 1000:
    print("Gotta atleast break even next time.")
    print(f"Final balance: {player_chips}")
elif player_chips < 2000:
    print("Wow you actually made some money.")
    print(f"Final balance: {player_chips}")
else:
    print("DAMN, we've got a BIG winner!")
    print(f"Final balance: {player_chips}")