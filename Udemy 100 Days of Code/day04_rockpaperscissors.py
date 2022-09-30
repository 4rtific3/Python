rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

win = True
user = input('Rock or Paper or Scissors\n').lower()

# match user_input:
#     case "rock":
#         print()

if user == "rock":
    user = 0
elif user == "paper":
    user = 1
elif user == "scissors":
    user = 2

rps_list = [rock, paper, scissors]
com = random.randint(0,2)

if user == com:
    win = ""
elif user > com:
    if user == 2 and com == 0:
        win = False
    else:
        win = True
elif user == 0 and com == 2:
    win = True
else:
    win = False

print('You:\n' + rps_list[user] + '\nComputer:\n' + rps_list[com])
if win == True:
    print("You win")
elif win == False:
    print("You lose")
else:
    print("It's a draw")