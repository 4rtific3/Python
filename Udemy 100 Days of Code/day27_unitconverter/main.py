from tkinter import *

CONVERSION_TABLE = {
    "km-miles": 0.621371,
    "m-inches": 39.3701,
    "l-gallons": 0.2641720524,
    "kg-pounds": 2.20462,
}

window = Tk()
window.title("Metric-Imperial Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

const = Label(text="1")

equal_text = Label(text="is equal to")
equal_text.grid(column=0, row=1)

unit1 = Label(text="km")
unit1.grid(column=2, row=0)

unit2 = Label(text="miles")
unit2.grid(column=2, row=1)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)
input.focus()

def calculate():
    conversion = listbox.get(listbox.curselection())
    converted_value["text"] = round((float(input.get()) * CONVERSION_TABLE[conversion]) ** float(const["text"]), 2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

def swap_units():
    unit_placeholder = unit1["text"]
    unit1["text"] = unit2["text"]
    unit2["text"] = unit_placeholder
    
    value_placeholder = converted_value["text"]
    converted_value["text"] = input.get()
    input.delete(0, END)
    input.insert(0, value_placeholder)
    
    if const["text"] == "1":
        const["text"] = "-1"
    else:
        const["text"] = "1"

swap_button = Button(text="Swap", command=swap_units)
swap_button.grid(column=2, row=2)

def reset_converter(unit_1, unit_2):
    unit1.config(text=unit_1)
    unit2.config(text=unit_2)
    input.delete(0, END)
    input.insert(0, 1)
    calculate()


# Listbox is not very effective here as highligting the value in the input box
# removes the listbox selection and results in an error
# May be better to use radio buttons instead
def listbox_used(event):
    selection = listbox.get(listbox.curselection())
    if selection == "km-miles":
        reset_converter("km", "miles")
    elif selection == "m-inches":
        reset_converter("m", "inches")
    elif selection == "l-gallons":
        reset_converter("l", "gallons")
    elif selection == "kg-pounds":
        reset_converter("kg", "pounds")

listbox = Listbox(height=4)
fruits = ["km-miles", "m-inches", "l-gallons", "kg-pounds"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=3, row=1)

window.mainloop()