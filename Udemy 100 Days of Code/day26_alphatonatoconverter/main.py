import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

convert = input("Enter a word: ").upper()
result = [nato_dict[i] for i in convert]

print(result)