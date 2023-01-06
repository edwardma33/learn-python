import random

words = ["camel", "mantis", "hello", 'world']

#picked_word = words[random.randint(0, len(words) - 1)]

picked_word = words[0]
print(picked_word)

final_word = []

check_list = []

def main():
    picked_letter = input("Pick a letter: ")
    
    

    for i in picked_word:
        if i == picked_letter:
            check_list.append(i)
        elif len(check_list) == 0 and i != picked_letter:
            check_list.append("_")
    print(check_list)
    
    if "".join(check_list) == picked_word:
        print("win")
    else:
        main()

main()