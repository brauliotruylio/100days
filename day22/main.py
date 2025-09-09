# Construir o jogo pong.
# Criar a tela
# Criar uma raquete e movimento
# Criar a outra raquete e movimento
# Criar a bola e movimento
# Detectar a colisão com as paredes e quique
# Detectar colisão com as raquetes
# detectar quando a raquete erra
# Manter score

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Desliga as animações automáticas

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detectar colisão com as paredes
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar colisão com as raquetes
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detectar quando a raquete erra
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.clear()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.clear()
        scoreboard.update_scoreboard()





screen.exitonclick()
