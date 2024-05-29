from Checking import Checking
from config import X_gamer, O_gamer, Field
  
def show_field():
    for i in Field.game_field:
        print(*i)
    print('\n-------------------\n')


def change_positions_g_1(position, sign):
    Field.list_of_positions.remove(position)
    gamer_1.positions.append(position)
    if sign == "x":
        if position[0] == "1":
            Field.game_field[1] = Checking.change_field_x(position, Field.game_field[1][0])
        elif position[0] == "2":
            Field.game_field[2] = Checking.change_field_x(position, Field.game_field[2][0])
        elif position[0] == "3":
            Field.game_field[3] = Checking.change_field_x(position, Field.game_field[3][0])
    else:
        if position[0] == "1":
            Field.game_field[1] = Checking.change_field_o(position, Field.game_field[1][0])
        elif position[0] == "2":
            Field.game_field[2] = Checking.change_field_o(position, Field.game_field[2][0])
        elif position[0] == "3":
            Field.game_field[3] = Checking.change_field_o(position, Field.game_field[3][0])
    show_field()
    res = Checking.check_winner(gamer_1.positions)
    if res:
        print(f"Победили {gamer_1.name}")
        gamer_1.winner = True
        return True
    else:
        gamer_2.count += 1
        return False

def change_positions_g_2(position, sign):
    Field.list_of_positions.remove(position)
    gamer_2.positions.append(position)
    if sign == "x":
        if position[0] == "1":
            Field.game_field[1] = Checking.change_field_x(position, Field.game_field[1][0])
        elif position[0] == "2":
            Field.game_field[2] = Checking.change_field_x(position, Field.game_field[2][0])
        elif position[0] == "3":
            Field.game_field[3] = Checking.change_field_x(position, Field.game_field[3][0])
    else:
        if position[0] == "1":
            Field.game_field[1] = Checking.change_field_o(position, Field.game_field[1][0])
        elif position[0] == "2":
            Field.game_field[2] = Checking.change_field_o(position, Field.game_field[2][0])
        elif position[0] == "3":
            Field.game_field[3] = Checking.change_field_o(position, Field.game_field[3][0])
    show_field()
    res = Checking.check_winner(gamer_2.positions)
    if res:
        print(f"Победили {gamer_2.name}")
        gamer_2.winner = True
        return True
    else:
        gamer_1.count += 1
        return False

def fighting():
    while len(Field.list_of_positions) > 0:
        if gamer_1.count > gamer_2.count and gamer_1.sign == "x":
            print("Ходят крестики\n-------------------\n")
            show_field() 
            position = input(f'Выберите позицию из списка {Field.list_of_positions}: ')
            if position not in Field.list_of_positions:
                print("Ошибка! Такой позиции не существует")
            else:
                win = change_positions_g_1(position, sign="x")
                if win:
                    break
        elif gamer_1.count > gamer_2.count and gamer_1.sign == "o":
            print("Ходят нолики\n-------------------\n")
            show_field()
            position = input(f'Выберите позицию из списка {Field.list_of_positions}: ')
            if position not in Field.list_of_positions:
                print("Ошибка! Такой позиции не существует")
            else:
                win = change_positions_g_1(position, sign="o")
                if win:
                    break
        else:
            if gamer_2.sign == "x":
                print("Ходят крестики\n-------------------\n")
                show_field() 
                position = input(f'Выберите позицию из списка {Field.list_of_positions}: ')
                if position not in Field.list_of_positions:
                    print("Ошибка! Такой позиции не существует")
                else:
                    win = change_positions_g_2(position, sign="x")
                    if win:
                        break
            else:
                print("Ходят нолики\n-------------------\n")
                show_field()
                position = input(f'Выберите позицию из списка {Field.list_of_positions}: ')
                if position not in Field.list_of_positions:
                    print("Ошибка! Такой позиции не существует")
                else:
                    win = change_positions_g_2(position, sign="o")
                    if win:
                        break


while True:
    x_or_o = input("Выберите, чем будете играть: x/o\n")
    if x_or_o.strip().lower() == "x":
        print("Игрок 1: X\nИгрок 2: O")
        gamer_1 = X_gamer()
        gamer_2 = O_gamer()
        gamer_2.count = -1
        break
    elif x_or_o.strip().lower() == "o":
        print("Игрок 1: O\nИгрок 2: X")
        gamer_1 = O_gamer()
        gamer_2 = X_gamer()
        gamer_2.count = -1
        break
    else:
        print("Ошибка! Введите X или O для продолжения")
        continue

fighting()

if gamer_1.winner is False and gamer_2.winner is False:
    print("Ничья!")
