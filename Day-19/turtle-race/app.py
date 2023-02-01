from turtle import Turtle, Screen
from random import *

t_1 = Turtle()
t_1.color('red')
t_2 = Turtle()
t_2.color('orange')
t_3 = Turtle()
t_3.color('yellow')
t_4 = Turtle()
t_4.color('green')
t_5 = Turtle()
t_5.color('blue')

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()

racers = [t_1, t_2, t_3, t_4, t_5]
colors = ['red', 'orange', 'yellow', 'green', 'blue']

screen = Screen()
screen.setup(width=600, height=400)

# Start Positions and Finish Line
def start_pos():
    start_y = 100
    for racer in racers:
        racer.penup()
        racer.goto(-250, start_y)
        start_y -= 50

def draw_f_line():
    finish_line.goto(250, -300)
    finish_line.pendown()
    finish_line.goto(250, 300)
###
# Operations
def all_move():
    for racer in racers:
        racer.forward(randint(1, 3) * 5)


###

def main():
    draw_f_line()
    start_pos()
    far = 0
    while far < 250:
        for i in racers:
            if i.xcor() - far > 0:
                far = i.xcor()
            else:
                racers.pop(racers.index(i))
        if far >= 250:
            print("W")
        else:
            all_move()

    

main()



screen.exitonclick()