from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_inputs():
    website_input.delete(0, END)
    password_input.delete(0, END)

def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if website == "" or password == "" or email == "":
        messagebox.showinfo(title="Error", message="Please do not leave any of the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as df:
                    data = json.load(df)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as df:
                    json.dump(new_data, df, indent=4)
            else:
                with open("data.json", "w") as df:
                    json.dump(data, df, indent=4)
            finally:
                clear_inputs()

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_input.get().title()
    
    if website == "":
        messagebox.showinfo(title="Error", message="Please do not leave website field empty")
    else:  
        try:
            with open("data.json", "r") as df:
                data = json.load(df)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found. Please add an account first")
        else:
            if website in data:
                account_details = data[website]
                account_user = account_details["email"]
                account_pass = account_details["password"]
                messagebox.showinfo(title="Account Details", message=f"Here are your account details for {website}:\nUsername: {account_user}\nPassword: {account_pass}")
            else:
                messagebox.showinfo(title="Error", message=f"You have not saved the account details from {website}")
                

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

website_search_button = Button(text="Search", command=search_website)
website_search_button.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "name@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

gen_pass_button = Button(text="Generate Password", command=generate_pw)
gen_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()