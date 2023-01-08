letters = "abcdefghijklmnopqrstuvwxyz"

letters_list = [*letters]

letters_list += letters_list
print(letters_list)

pseudo_str = ""


def encrypt(word, shift):
    global pseudo_str

    if shift > 26:
        encrypt(word, input("How much displacement?\n"))

    for i in word:
        pseudo_char = letters_list[letters_list.index(i) + int(shift)]
        pseudo_str += pseudo_char
    print(pseudo_str)

def decode():
    print("y'all hoes")

encrypt(input("Write here...\n"), input("How much displacement?\n"))



