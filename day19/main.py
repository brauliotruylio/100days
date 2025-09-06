import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Faça sua aposta", prompt="Qual a cor que você quer apostar?")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for race_turtle in all_turtles:
        # Verifica se alguma tartaruga cruzou a linha de chegada
        if race_turtle.xcor() > 230:
            is_race_on = False
            winning_color = race_turtle.pencolor()
            if winning_color == user_bet:
                print(f"Você venceu! A cor vencedora foi {winning_color}")
            else:
                print(f"Você perdeu! A cor vencedora foi {winning_color}")
            break  # Para o loop for imediatamente após encontrar um vencedor

        rand_distance = random.randint(0, 10)
        race_turtle.forward(rand_distance)
screen.exitonclick()
