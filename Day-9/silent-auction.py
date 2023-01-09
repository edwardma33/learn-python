### This block was found with a stack overflow search
import os

def clear():
    os.system('clear')
###
clear()
print("Welcome to the silent auction!")

bid_list = {}

def place_bid(name, bid):
    bid_list[name] = int(bid)
    
def find_winner():
    clear()
    winning_bidder = ""
    winning_bid = 0
    for bidder in bid_list:
        if winning_bid - bid_list[bidder] < 0:
            winning_bidder = bidder
            winning_bid = bid_list[bidder]
    print(f"{winning_bidder} wins with a bid of: ${winning_bid}")

def ask_for_bid():
    if input("Would you like to place a bid? (y/n)\n") == "y":
        place_bid(input("What is your name?\n"), input("How much would you like to bid\n$ "))
        clear()
        ask_for_bid()
    else:
        find_winner()



ask_for_bid()