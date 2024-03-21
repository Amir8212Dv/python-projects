from screen import GameScreen
from player import Player
from ball import Ball

screen = GameScreen()
left_player = Player("left")
right_player = Player("right")

screen.set_players(left_player, right_player)
ball = Ball(left_player, right_player, screen.refresh, screen.switch_player_turn)
screen.refresh()

screen.screen.exitonclick()
