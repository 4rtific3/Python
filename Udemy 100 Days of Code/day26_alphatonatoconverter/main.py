import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    convert = input("Enter a word: ").upper()
    
    try:
        result = [nato_dict[i] for i in convert]
    except KeyError:
        print("Only letters in the alphabet please")
    else:
        print(result)
        break