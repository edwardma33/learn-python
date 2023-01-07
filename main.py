import random

words = ["camel", "mantis", "hello", 'world']

#picked_word = words[random.randint(0, len(words) - 1)]

picked_word = words[0]
print(picked_word)


final_word = []
for i in picked_word:
    final_word.append("-")
print(final_word)

lives_left = 6
 
letters_correct = 0

check_word = 0
print(check_word)



def letter_check():
    global lives_left
    global check_word 

    picked_letter = input("Pick a letter: ")

    for i in picked_word:
        if picked_letter == i:
            final_word[picked_word.index((i))] = f"{i}"
            check_word += 1
            print(f"letters_correct: {check_word}")
        else:
            lives_left -= 1
            print(f"Lives: {lives_left}")
            
    print(final_word)

def win_check():
    if check_word == len(final_word):
        print("win")
    elif lives_left == 0:
        print("Dead")
    else:
        main()



def main():
    letter_check()
    
    win_check()
    

main()