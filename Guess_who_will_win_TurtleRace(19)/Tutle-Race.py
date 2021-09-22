from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle win the race? Enter a Color: ")
#print(user_input)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()