letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(len(letters))

def encrypt(word, shift):
    word = [*word]
    for i in word:
        word[word.index(i)] = letters[letters.index(i) + int(shift)]
    print(word)

encrypt(input("Write here...\n"), input("How much displacement?\n"))