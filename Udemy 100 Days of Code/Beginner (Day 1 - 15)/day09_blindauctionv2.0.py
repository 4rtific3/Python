import os
import day9_blindauctionart as art

def clear_terminal():
    os.system('cls||clear')

def new_bid_name():
    name = input("What is your name?\n")
    return name

def new_bid_value():
    bid_value = input("What is your bid?\n$")
    while True:
        if bid_value.isnumeric():
            return int(bid_value)
        else:
            print("Please enter a valid bid amount.")
            bid_value = input("What is your bid?\n$")

def new_input():
    next_bidder = input("Is there another bidder? Y/N\n").lower()
    while True:
        if next_bidder == "y":
            return True
        elif next_bidder == "n":
            return False
        else:
            print('Please input "Y" or "N"')
            next_bidder = input("Is there another bidder? Y/N\n").lower()

def max_bid(bidders):
    highest_bid = ["", 0]
    for i in bidders:
        if bidders[i] > highest_bid[1]:
            highest_bid[0] = i
            highest_bid[1] = bidders[i]
    return highest_bid[0], highest_bid[1]

def run():
    bidders = {}
    result = True

    print(art.logo)

    while result:
        name = new_bid_name()
        bid = new_bid_value()
        bidders[name] = bid
        result = new_input()
        clear_terminal()

    name,bid = max_bid(bidders)
    
    print(f"{name} won the bid with a value of ${bid}")

run()