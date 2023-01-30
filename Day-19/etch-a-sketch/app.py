from turtle import Turtle, Screen

tim = Turtle()
tim.speed('fastest')

screen = Screen()
screen.title("Etch-A-Sketch")

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

screen.listen()
screen.onkey(move_forward, 'space')
screen.onkey(turn_left, 'Left')
screen.onkey(turn_right, 'Right')
screen.onkey(tim.penup, 'Up')
screen.onkey(tim.pendown, 'Down')
screen.onkey(tim.clear, 'c')
screen.onkey(tim.reset, 'C')

# Keep bottom!
screen.exitonclick()