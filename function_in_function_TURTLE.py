import turtle
from turtle import Turtle, Screen

tu = turtle
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    # tim.left(90)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    # tim.left(-90)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

# def counter_clockwise():
#     tim.circle(100, extent=90)
#
# def clockwise():
#     #tim.setheading(180)
#     tim.circle(200, extent=-210)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()



# W = forwards
# S = backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

