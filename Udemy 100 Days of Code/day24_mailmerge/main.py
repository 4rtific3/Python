PLACEHOLDER = "[name]"


with open("Input/Letters/starting_letter.txt") as letter:
    template = letter.read()


with open("Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        stripped_name = name.strip()
        modified_name = template.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as copy:
            copy.write(modified_name)