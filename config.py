class X_gamer:
    def __init__(self):
        self.name = "Крестики"
        self.sign = "x"
        self.positions = []
        self.count = 0
        self.winner = False


class O_gamer:
    def __init__(self):
        self.name = "Нолики"
        self.sign = "o"
        self.positions = []
        self.count = 0
        self.winner = False

class Field:
    game_field = [["    1   2   3"],
                  ["1 | ~ | ~ | ~ |"],
                  ["2 | ~ | ~ | ~ |"],
                  ["3 | ~ | ~ | ~ |"]]
    list_of_positions = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]