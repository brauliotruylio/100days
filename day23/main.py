import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()

def play_game():
    """Executa uma rodada do jogo Turtle Crossing."""
    screen.clear()  # Limpa a tela para um novo jogo
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detecta colisão com carro
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detecta cruzamento bem-sucedido
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

play_game()

while True:
    resposta = screen.textinput("Jogar Novamente?", "Deseja jogar novamente? Digite 's' para sim ou 'n' para não:")
    if resposta and resposta.lower() == 's':
        play_game()
    else:
        break

screen.bye()
