import random
import day14_higherlowerfiles as files
import os

DATA = files.data

def clear_screen():
    os.system('cls||clear')

def start():
    print(files.logo)
    print("Welcome to Higher or Lower! The aim of the game is to guess who has more followers")

def select_people(used_data, counter):
    no_data = len(used_data)
    if counter == 0:
        i = 2
    else:
        i = 1
    while len(used_data) < no_data + i:
        random_data = random.choice(DATA)
        if random_data not in used_data:
            used_data.append(random_data)

def print_choices(used_data, counter, correct_ans, compare_data):
    if counter == 0:
        choice1 = used_data[correct_ans]
    else:
        choice1 = compare_data[correct_ans]
    choice2 = used_data[counter+1]
    compare_data[0] = choice1
    compare_data[1] = choice2
    print(f'\n{choice1["name"]}, {choice1["description"]}, {choice1["country"]}')
    print(files.vs)
    print(f'{choice2["name"]}, {choice2["description"]}, {choice2["country"]}\n')
    if choice1["follower_count"] > choice2["follower_count"]:
        return 0, compare_data
    else:
        return 1, compare_data

def select_choice():
    while True:
        guess = input('Who has more followers? Type "1" or "2" to choose: ')
        if guess == "1":
            return 0
        elif guess == "2":
            return 1
        else:
            print(f'Please type "1" or "2"')

def check_guess(compare_data, counter, guess, correct_ans):
    wrong_ans = 1
    if correct_ans == 1:
        wrong_ans = 0
    correct_name = compare_data[correct_ans]["name"]
    correct_followers = compare_data[correct_ans]["follower_count"]
    wrong_name = compare_data[wrong_ans]["name"]
    wrong_followers = compare_data[wrong_ans]["follower_count"]
    if guess == correct_ans:
        print(f'Correct! {correct_name} has {correct_followers} followers and {wrong_name} has {wrong_followers} followers.')
        return correct_ans, False
    else:
        print(f'Nope, {correct_name} has {correct_followers} followers and {wrong_name} has {wrong_followers} followers.')
        return guess, True

def play_again():
    while True:
        again = input("Would you like to play again? Y/N: ").lower()
        if again == "y":
            return True
        elif again == "n":
            print("Thank you for playing!")
            return False
        else:
            print('Please type "Y" or "N"')

def play():
    again = True
    while again:
        clear_screen()
        used_data = []
        compare_data = [{},{}]
        round = 0
        lose = False
        correct_ans = 0
        start()
        while not lose:
            select_people(used_data, round)
            correct_ans, compare_data = print_choices(used_data, round, correct_ans, compare_data)
            guess = select_choice()
            correct_ans, lose = check_guess(compare_data, round, guess, correct_ans)
            round += 1
        again = play_again()
    
play()