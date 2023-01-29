from turtle import Turtle, Screen, colormode
import random

colormode(255)
colors = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37)]

tim = Turtle()

def plot():
    tim.dot(20, colors[random.randint(0, len(colors) - 1)])

def start_position():
    tim.hideturtle()
    tim.penup()
    tim.speed('fastest')
    tim.right(135)
    tim.forward(500)
    tim.left(135)
    plot()

def gen_piece(dots_per_line, spacing):
    num_dots = 1
    start_position()

    while num_dots < dots_per_line ** 2:
        if num_dots == 0 or num_dots % dots_per_line != 0:
            tim.forward(spacing)
            plot()
            num_dots += 1
        elif (num_dots / dots_per_line) % 2 == 0:
            tim.right(90)
            tim.forward(spacing)
            tim.right(90)
            plot()
            num_dots += 1
        else:
            tim.left(90)
            tim.forward(spacing)
            tim.left(90)
            plot()
            num_dots += 1
 
# Call Functions Here!

gen_piece(10, 50)

# Keep bottom!
screen = Screen()
screen.exitonclick()