import os
def clear():
    os.system('clear')
clear()
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color('green')
tim.pensize(6)
tim.speed('fast')

# Challenge 1: Draw a square
def draw_square():
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)

# Challenge 2: Draw a dashed line
def dash_line(set_length):
    for i in range(set_length):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

# Challenge 3A: Draw each shape from triangle to decagaon
def draw_shape(sides):
    angle = 360 / sides
    
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

def draw_all():
    for i in range(3, 11):
        draw_shape(i)

# Challenge 3B: Make each line in 3A a random color
def draw_shape_2(sides):
    angle = 360 / sides
    
    for i in range(sides):
        tim.color(colors[random.randint(0, len(colors) - 1)])
        tim.forward(100)
        tim.right(angle)

def draw_all_2():
    for i in range(3, 11):
        draw_shape_2(i)

# Challenge 4: Create a random walk
def gen_rand_walk(iterations):
    for i in range(iterations):
        tim.color(colors[random.randint(0, len(colors) - 1)])
        tim.right(random.randint(0, 360))
        tim.forward(40)

# Call functions here!

gen_rand_walk(100)

#Keep bottom 
screen = Screen()
screen.exitonclick()