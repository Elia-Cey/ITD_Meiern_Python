from src.Player import Player


class Round:
    def __init__(self, players):
        self.players = players

    def play(self):
        results = { player: player.make_move() for player in self.players }

        loser = min(results, key=results.get)
        loser.add_points()

        print(f"Verlierer der Runde: {loser.name}")
        return loser

    def show_scores(self):
        print("\n--- Punktestand --- ")
        for player in self.players:
            print(f"{player.name}: {player.points}")
        print("-------------------\n")