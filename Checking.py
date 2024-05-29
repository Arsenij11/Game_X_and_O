class Checking:
    @staticmethod
    def change_field_x(position, field):
        if position[1] == "1":
            field = field[:4] + "x" + field[5:]
        elif position[1] == "2":
            field = field[:8] + "x" + field[9:]
        elif position[1] == "3":
            field = field[:12] + "x" + field[13:]
        return [field]
    @staticmethod
    def change_field_o(position, field):
        if position[1] == "1":
            field = field[:4] + "o" + field[5:]
        elif position[1] == "2":
            field = field[:8] + "o" + field[9:]
        elif position[1] == "3":
            field = field[:12] + "o" + field[13:]
        return [field]
    @staticmethod
    def check_winner(positions):
        positions = list(map(int, positions))
        if 11 in positions and 12 in positions and 13 in positions:
            return True
        elif 21 in positions and 22 in positions and 23 in positions:
            return True
        elif 31 in positions and 32 in positions and 33 in positions:
            return True
        elif 11 in positions and 21 in positions and 31 in positions:
            return True
        elif 12 in positions and 22 in positions and 32 in positions:
            return True
        elif 13 in positions and 23 in positions and 33 in positions:
            return True
        elif 11 in positions and 22 in positions and 33 in positions:
            return True
        elif 13 in positions and 22 in positions and 31 in positions:
            return True
        else:
            return False


            

    