import os
import day9_blindauctionart as art

def clear_terminal():
    os.system('cls||clear')

print(art.logo)

bidders = {}

def add_new_bidder(name, bid):
    bidders[name] = bid

def new_input():
    global new_bidder
    next_bidder = input("Is there another bidder? Y/N\n").lower()
    if next_bidder == "y":
        new_bidder = True
    elif next_bidder == "n":
        new_bidder = False
    else:
        print('Please input "Y" or "N"')
        new_input()


new_bidder = True

while new_bidder:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    add_new_bidder(name, bid)
    new_input()
    clear_terminal()

highest_bid = ["", 0]

for i in bidders:
    if bidders[i] > highest_bid[1]:
        highest_bid[0] = i
        highest_bid[1] = bidders[i]

print(f"{highest_bid[0]} won the bid with a value of ${highest_bid[1]}")