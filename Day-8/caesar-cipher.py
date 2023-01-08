letters = "abcdefghijklmnopqrstuvwxyz"
letters_list = [*letters]
letters_list += letters_list

pseudo_str = ""

def decode(word, shift):
    pseudo_str = ""
    for i in word:
        if i != " ":
            pseudo_char = letters_list[letters_list.index(i) - int(shift)]
            pseudo_str += pseudo_char
        else:
            pseudo_char = " "
            pseudo_str += pseudo_char
    
    print(f"Decoded message: {pseudo_str}")

def encrypt(word, shift):
    global pseudo_str
    if int(shift) > 26 or len(word) == 0:
        print("Error:\nMust be 1 or more characters\nDiplacement must be <= 26")
        encrypt(input("Write here...\n"), input("How much displacement?\n"))
    else:
        for i in word:
            if i != " ":
                pseudo_char = letters_list[letters_list.index(i) + int(shift)]
                pseudo_str += pseudo_char
            else:
                pseudo_char = " "
                pseudo_str += pseudo_char
        print(f"Encrypted message: {pseudo_str}")
        if input("Decode? (y/n)\n") == "y":
             decode(pseudo_str, shift)


if input("Would you like to encrypt or decode a message?\ne: encrypt\nor\nd: decode") == "e":
    encrypt(input("Write here...\n"), input("How much displacement?\n"))
else:
    decode(input("Write here...\n"), input("How much displacement?\n"))





