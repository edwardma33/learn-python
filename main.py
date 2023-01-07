import random

words = ["camel", "mantis", "hello", 'world']

picked_word = words[random.randint(0, len(words) - 1)]


final_word = []
for i in picked_word:
    final_word.append("-")
print(final_word)

lives_left = 6
 
letters_correct = 0

check_word = 0

lost_life_condition = []
for i in final_word:
    lost_life_condition.append("nope")


#Above here is all setup



def letter_check():
    global lost_life_condition
    global lives_left
    global check_word
    global picked_word

    lost_life_check = []

    picked_letter = input("Pick a letter: ")

    for i in picked_word:
        if i == picked_letter:
            final_word[picked_word.index(i)] = i
        else:
            lost_life_check.append("nope")
    
    if lost_life_check == lost_life_condition:
        lives_left -= 1
            
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