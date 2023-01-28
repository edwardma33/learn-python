import os
def clear():
    os.system('clear')
import random
from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))
perfect_score = len(question_bank)
current_question = ''
current_answer = ''
points = 0

def ask_question():
    global current_answer
    question_num = random.randint(0, len(question_bank) - 1)
    current_question = question_bank[question_num].text
    current_answer = question_bank[question_num].answer[0]
    question_bank.pop(question_num)
    print(current_question)

def eval_answer():
    global points
    if input("[T/F]: ").upper() == current_answer:
        points += 1

while len(question_bank) > 0:
    clear()
    ask_question()
    eval_answer()


print(f'You got {points} of {perfect_score} questions correct!')
print(f"That's {int(round(points / perfect_score, 2) * 100)}%")
