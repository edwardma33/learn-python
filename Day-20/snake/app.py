from turtle import Turtle, Screen, time
# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake")

# Make snake body
snake = []
for i in range(0,3):
    new_seg = Turtle('square')
    new_seg.penup()
    new_seg.color('white')
    new_seg.goto(-20 * i, 0)
    snake.append(new_seg)

screen.update()

# Move snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)
    # This loop moves each square into the position of the square ahead of it
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

# Control snake

# Detect collision with food

# Create scoreboard

# Detect collision with the wall AND tail

# Keep bottom!
screen.exitonclick()