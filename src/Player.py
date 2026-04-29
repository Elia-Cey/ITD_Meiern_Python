import random

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def make_move(self):
        while True:
            try:
                move_1 = random.randint(1,6)
                move_2 = random.randint(1,6)

                move = int(input(f"{self.name}, git deinen Wurf ein: "))
                if 1 <= move <= 6:
                    return move
                else:
                    print("Bitte eine Zahl zwischen 1 und 6 eingeben.")
            except Exception as e:
                print("Ungültige Eingabe! Ganzzahl erforderlich.\n", e)


    def add_points(self):
        self.points += 1
