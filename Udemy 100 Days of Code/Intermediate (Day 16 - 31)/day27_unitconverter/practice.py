import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI Intro")
window.minsize(width=500, height=300)

# Adding padding for individual objects
window.config(padx=20, pady=20)

# Creating labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.grid(column=0, row=0)

# Changing label values, 2 methods
my_label["text"] = "New Text"
my_label.config(text="Newer Text")

def button_clicked():
    my_label["text"] = input.get()

#Creating buttons
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Creating entries
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()