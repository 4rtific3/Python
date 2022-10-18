from tkinter import *
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
random_french_word = ""

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data.to_csv("data/words_to_learn.csv", index=0)

# How to convert DataFrame into dictionary with 2 columns as key-value pair
# Option 1: Convert into pandas Series
# pd.Series(df.name.values,index=df.state).to_dict()
# Option 2: Set the index (key) and apply to_dict()["value"] to append the values to the keys
data_dict = data.set_index("French").to_dict()["English"]

# Resetting words after clicking a button
def new_card():
    global random_french_word, flip_timer
    window.after_cancel(flip_timer)
    random_french_word = random.choice(list(data_dict.keys()))
    canvas.itemconfig(canvas_side, image=card_front)
    canvas.itemconfig(canvas_word, text=f"{random_french_word}", fill="black")
    canvas.itemconfig(canvas_title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)
    

def flip_card():
    canvas.itemconfig(canvas_side, image=card_back)
    canvas.itemconfig(canvas_word, text=f"{data_dict[random_french_word]}", fill="white")
    canvas.itemconfig(canvas_title, text="English", fill="white")
    
def word_known():
    data_dict.pop(random_french_word)
    
    # Writing a dictionary to a csv file with new header
    with open('data/words_to_learn.csv', 'w', encoding='utf-8-sig', newline='') as df:
        header_key = ["French", "English"]
        new_val = csv.DictWriter(df, fieldnames=header_key)

        new_val.writeheader()
        for key in data_dict:
            new_val.writerow({'French': key, 'English': data_dict[key]})
    new_card()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_side = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_card)
no_button.grid(column=0, row=1)

yes_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=word_known)
yes_button.grid(column=1, row=1)

new_card()

window.mainloop()