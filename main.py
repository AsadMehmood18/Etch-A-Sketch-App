from turtle import Turtle,Screen
bob = Turtle()
screen = Screen()


def move_forwards():
    bob.forward(10)
def move_backwards():
    bob.backward(10)
def move_clockwise():
    new_heading = bob.heading()-10
    bob.setheading(new_heading)
def move_counter_clockwise():
    new_heading = bob.heading()+10
    bob.setheading(new_heading)
def clear_drawing():
    screen.resetscreen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()