from InputHelper import *
from Player import *
from AIPlayer import *
from Round import *

class Game:
    def __init__(self):
        self.players =[]

    def setup(self):
        total_players = InputHelper.get_player_input(
            "Wie viele Spieler insgesamt?", 2, 10
        )

        real_players = InputHelper.get_player_input(
            "Wie viele echte Spieler? ", 1, total_players
        )

        for i in range(real_players):
            name = input(f"Name von Spieler {i+1}: ")
            self.players.append(Player(name))

        for i in range (total_players - real_players):
            
            self.players.append(AIPlayer(f"KI_{i+1}"))



    def start(self):
        self.setup()

        for i in range(3):
            print(f"\n--- Runde {i+1} ---")
            round = Round(self.players)
            round.play()
            round.show_scores()
