############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
# Player draws first

import random
import os
import day11_capstone_blackjackart as art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end = False
game_round = 0




def clear_screen():
    os.system('cls||clear')

def start():
    dealer_first_card = 0
    dealer_score = 0
    player_score = 0
    for i in range(4):
        draw = random.choice(cards)
        if i == 1:
            dealer_first_card = draw
        if (i+1) % 2 == 0:
            dealer_score += draw
        else:
            player_score += draw
    return player_score, dealer_score, dealer_first_card

# Drawing card and changing Ace to 1 if score exceeds 21
def draw(score):
    draw = random.choice(cards)
    if score + draw > 21 and draw == 11:
        draw = 1
    return draw

def draw_again():
    while True:
        draw = input('Do you want to "stand" or "hit"? ').lower()
        if draw == "hit":
            return False
        elif draw == "stand":
            return True
        else:
            print('Please type "stand" or "hit"')

def dealer_draw(dealer_score):
    while dealer_score < 17:
        dealer_score += random.choice(cards)
    return dealer_score
    
def win_check(player_score, dealer_score):
    if player_score > 21:
        return False
    elif player_score > dealer_score:
        return True
    elif dealer_score > 21:
        return True
    else:
        return False

def check_natural(player_score, dealer_score):
    if player_score == 21:
        return 1
    elif player_score == 21 and dealer_score == 21:
        return 2
    elif dealer_score == 21:
        return 3

def play_again():
    while True:
        again = input("Would you like to play again? Y/N\n").lower()
        if again == "y":
            clear_screen()
            blackjack()
        elif again == "n":
            print("Thanks for playing! Goodbye!")
            return
        else:
            print('Please type "Y" or "N"')

def blackjack():
    print(art.logo)
    player_score, dealer_score, dealer_first_card = start()
    natural = check_natural(player_score, dealer_score)
    if natural == 1:
        print("Blackjack! You win!")
    elif natural == 2:
        print("You and the dealer both got a blackjack! Tie!")
    elif natural == 3:
        print("The dealer got a blackjack! You lose.")
    else:
        print(f"Your starting score is {player_score} and the dealer's first card is {dealer_first_card}")
        end = draw_again()
        while not end:
            card = draw(player_score)
            player_score += card
            if player_score >= 21:
                end = True
            print(f"Your score is {player_score}")
            if player_score < 21:
                end = draw_again()
        dealer_score = dealer_draw(dealer_score)
        print(f"The dealer's final score is {dealer_score}")
        win = win_check(player_score, dealer_score)
        if win == True:
            print("You win!")
        else:
            print("You lose")
        play_again()

blackjack()