from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets!", prompt="Choose a color of the rainbow")

colors = ["red", "blue", "green", "yellow", "orange","purple"]
y_positions = [-80, -50, -20, 10, 40, 70]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You Won! the winning turtle was {winning_turtle}")
            else:
                print(f"You lost! The winning turtle was {winning_turtle}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.clear()

screen.exitonclick()