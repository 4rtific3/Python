# Tried to code without using a list to store and compare current 2 options

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

def print_choices(used_data, counter, correct_ans):
    choice1 = used_data[correct_ans]
    choice2 = used_data[counter+1]
    print(f'\n{choice1["name"]}, {choice1["description"]}, {choice1["country"]}')
    print(files.vs)
    print(f'{choice2["name"]}, {choice2["description"]}, {choice2["country"]}\n')
    if choice1["follower_count"] > choice2["follower_count"]:
        return correct_ans
    else:
        return counter+1

def select_choice():
    while True:
        guess = input('Who has more followers? Type "1" or "2" to choose: ')
        if guess == "1":
            return 1
        elif guess == "2":
            return 2
        else:
            print(f'Please type "1" or "2"')

def check_guess(used_data, counter, guess, correct_ans):
    if correct_ans == 1 and counter == 0:
        wrong_ans = 0
    else:
        wrong_ans = counter+1
    correct_name = used_data[correct_ans]["name"]
    correct_followers = used_data[correct_ans]["follower_count"]
    wrong_name = used_data[wrong_ans]["name"]
    wrong_followers = used_data[wrong_ans]["follower_count"]
    if guess == 1:
        player_ans = used_data[correct_ans]["follower_count"]
    elif guess == 2:
        player_ans = used_data[counter+1]["follower_count"]
    if player_ans == used_data[correct_ans]["follower_count"]:
        print(f'Correct! {correct_name} has {correct_followers} followers and {wrong_name} has {wrong_followers} followers.')
        return correct_ans, False
    else:
        print(f'Nope, {correct_name} has {correct_followers} followers and {wrong_name} has {wrong_followers} followers.')
        return guess, True

def play():
    used_data = []
    round = 0
    lose = False
    correct_ans = 0
    start()
    while not lose:
        select_people(used_data, round)
        correct_ans = print_choices(used_data, round, correct_ans)
        guess = select_choice()
        correct_ans, lose = check_guess(used_data, round, guess, correct_ans)
        round += 1

play()