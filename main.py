from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win thr race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []


def make_turtles(number):
    y = -50
    for n in range(number):
        turtle = Turtle(shape='turtle')
        all_turtles.append(turtle)
        turtle.color(colors[n])
        turtle.pu()
        turtle.goto(-230, y)
        y += 25


make_turtles(6)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if round(turtle.xcor()) > 210:
            is_race_on = False
            win_color = turtle.pencolor()

if win_color == user_bet:
    print(f"Congrats! You won! The winner turtle is {win_color} turtle.")
else:
    print(f"Sorry you lose. The winner turtle is {win_color} turtle.")

screen.exitonclick()