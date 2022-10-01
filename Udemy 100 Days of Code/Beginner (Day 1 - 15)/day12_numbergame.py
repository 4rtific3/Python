import random
import os
import day12_numbergameart as art

def clear_screen():
    os.system('cls||clear')

# Setting the number of rounds based on difficulty level
def choose_difficulty():
    while True:
        difficulty = input('Choose your difficulty. "Easy" or "Hard": ').lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print('Please type "Easy" or "Hard"')

# Asks for number input between 1 and 100
# Informs the player if they have already guessed the number before
def guess(guess_list):
    while True:
        guess = input("Guess a number: ")
        try:
            guess = int(guess)
            if guess not in guess_list:
                if guess > 0 and guess < 101:
                    return int(guess)
                else:
                    print("Please type a number between 1 and 100")
            else:
                print("You've already guessed this number")
        except ValueError:
            print("Please type a number between 1 and 100")
\
# Checks the outcome of the round
# If the player guessed right, it breaks the while loop
def check(guess, actual, rounds):
    if guess < actual:
        print(f"Too low. You have {rounds} rounds left")
    elif guess > actual:
        print(f"Too high. You have {rounds} rounds left")
    else:
        print("You guessed the number! You win!")
        return True

def play_again():
    while True:
        cont = input('Would you like to play again? Y/N: ').lower()
        if cont == "y":
            return True
        elif cont == "n":
            print("Thank you for playing!")
            return False
        else:
            print('Please type "Y" or "N"')

def number_game():
    guesses = []
    print(art.logo)
    finish = False
    actual_no = random.randint(1, 100)
    rounds = choose_difficulty()
    print(f"You have {rounds} rounds to guess the correct number.")
    while not finish and rounds > 0:
        rounds -= 1
        player_guess = guess(guesses)
        guesses.append(player_guess)
        finish = check(player_guess, actual_no, rounds)
    if rounds == 0:
        print(f"The number was {actual_no}. You lose")
    if play_again():
        clear_screen()
        number_game()

number_game()