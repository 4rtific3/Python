import random
import day07_hangmanfiles as files

lives = 6
win = True

chosen_word = random.choice(files.word_list)
display = ["_" for i in chosen_word]
guesses = []

def end():
    global win
    if "".join(display) == chosen_word:
        win = True
        return True
    elif lives == 0:
        win = False
        return True

print(files.logo)
print("".join(display))

while not end():
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    
    if guess in guesses:
        print("You've already guessed this letter")
    elif guess not in chosen_word:
        lives -= 1
    
    if guess not in guesses:
        guesses.append(guess)

    print("".join(display))
    print(files.stages[lives])

    if end() and win:
        print("You win!")
    elif end() and not win:
        print(f"You lose\nThe word was: {chosen_word}")
