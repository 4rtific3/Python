alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import day8_art

def caesar(text, shift, direction):
    text_list = [i for i in text]
    for i in range(len(text)):
        if text[i] in alphabet:
            shifted_alpha = alphabet.index(text[i]) + shift
            if direction == "encode":
                while shifted_alpha > 25:
                    shifted_alpha -= 26
            elif direction == "decode":
                shifted_alpha = alphabet.index(text[i]) - shift
                while shifted_alpha < 0:
                    shifted_alpha += 26
            text_list[i] = alphabet[shifted_alpha]
    caesared = "".join(text_list)
    print(f"The {direction}d message is {caesared}")

restart = True
print(day8_art.logo)

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart_prompt = input("Would you like to continue? Y/N\n").lower()
    if restart_prompt == "n":
        restart = False