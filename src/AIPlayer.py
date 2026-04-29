from Player import *

class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = ""

    def make_move(self):
        move = random.randint(1,6)
        print(f"{self.name}[{self.type}] hat Wurf: {move}")
        return move

    def add_type(self):
        types = ["vorsichtig", "normal", "mutig"]
