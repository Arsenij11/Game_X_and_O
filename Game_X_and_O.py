def field_crosses(Str_0, Str_1, Str_2, Str_3, list_1):
    crosses(Str_0, Str_1, Str_2, Str_3, list_1)
def crosses(Str_0, Str_1, Str_2, Str_3, list_1):
    print(Str_0 + "\n" + Str_1 + "\n" + Str_2 + "\n" + Str_3)
    if list_1 == []:
        result = "Ничья!"
        print(result)
        return result
    position = input(f"Введите позицию {list_1}:")
    if position in list_1:
        list_1.remove(position)
        if position == "00":
            Str_1_changed = Str_1[:2] + "x" + Str_1[3:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "01":
            Str_1_changed = Str_1[:4] + "x" + Str_1[5:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "02":
            Str_1_changed = Str_1[:6] + "x" + Str_1[7:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "10":
            Str_2_changed = Str_2[:2] + "x" + Str_2[3:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "11":
            Str_2_changed = Str_2[:4] + "x" + Str_2[5:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "12":
            Str_2_changed = Str_2[:6] + "x" + Str_2[7:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "20":
            Str_3_changed = Str_3[:2] + "x" + Str_3[3:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2, Str_3_changed, list_1)
        elif position == "21":
            Str_3_changed = Str_3[:4] + "x" + Str_3[5:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2, Str_3_changed, list_1)
        elif position == "22":
            Str_3_changed = Str_3[:6] + "x" + Str_3[7:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, крестики победили":
                print(result)
                return result
            else:
                field_zeroes(Str_0, Str_1, Str_2, Str_3_changed, list_1)
    else:
        print(f"Ошибка, введите корректное число из списка {list_1}")
        field_crosses(Str_0, Str_1, Str_2, Str_3, list_1)


def field_zeroes(Str_0, Str_1, Str_2, Str_3, list_1):
    zeroes(Str_0, Str_1, Str_2, Str_3, list_1)


def zeroes(Str_0, Str_1, Str_2, Str_3, list_1):
    print(Str_0 + "\n" + Str_1 + "\n" + Str_2 + "\n" + Str_3)
    if list_1 == []:
        result = "Ничья!"
        print(result)
        return result
    position = input(f"Введите позицию {list_1}:")
    if position in list_1:
        list_1.remove(position)
        if position == "00":
            Str_1_changed = Str_1[:2] + "o" + Str_1[3:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "01":
            Str_1_changed = Str_1[:4] + "o" + Str_1[5:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "02":
            Str_1_changed = Str_1[:6] + "o" + Str_1[7:]
            result = check_winner(Str_0, Str_1_changed, Str_2, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1_changed, Str_2, Str_3, list_1)
        elif position == "10":
            Str_2_changed = Str_2[:2] + "o" + Str_2[3:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "11":
            Str_2_changed = Str_2[:4] + "o" + Str_2[5:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "12":
            Str_2_changed = Str_2[:6] + "o" + Str_2[7:]
            result = check_winner(Str_0, Str_1, Str_2_changed, Str_3)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2_changed, Str_3, list_1)
        elif position == "20":
            Str_3_changed = Str_3[:2] + "o" + Str_3[3:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2, Str_3_changed, list_1)
        elif position == "21":
            Str_3_changed = Str_3[:4] + "o" + Str_3[5:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2, Str_3_changed, list_1)
        elif position == "22":
            Str_3_changed = Str_3[:6] + "o" + Str_3[7:]
            result = check_winner(Str_0, Str_1, Str_2, Str_3_changed)
            if result == "Поздравляю, нолики победили":
                print(result)
                return result
            else:
                field_crosses(Str_0, Str_1, Str_2, Str_3_changed, list_1)
    else:
        print(f"Ошибка, введите корректное число из списка {list_1}")
        field_zeroes(Str_0, Str_1, Str_2, Str_3, list_1)


def check_winner(Str_0, Str_1, Str_2, Str_3):
    if (Str_1[2] == "x" and Str_1[4] == "x" and Str_1[6] == "x") or (
            Str_2[2] == "x" and Str_2[4] == "x" and Str_2[6] == "x") or (
            Str_3[2] == "x" and Str_3[4] == "x" and Str_3[6] == "x") or (
            Str_1[2] == "x" and Str_2[4] == "x" and Str_3[6] == "x") or (
            Str_1[2] == "x" and Str_2[2] == "x" and Str_3[2] == "x") or (
            Str_1[4] == "x" and Str_2[4] == "x" and Str_3[4] == "x") or (
            Str_1[6] == "x" and Str_2[6] == "x" and Str_3[6] == "x") or (
            Str_1[6] == "x" and Str_2[4] == "x" and Str_3[2] == "x"):
        print(Str_0 + "\n" + Str_1 + "\n" + Str_2 + "\n" + Str_3)
        result = "Поздравляю, крестики победили"
        return result
    elif (Str_1[2] == "o" and Str_1[4] == "o" and Str_1[6] == "o") or (
            Str_2[2] == "o" and Str_2[4] == "o" and Str_2[6] == "o") or (
            Str_3[2] == "o" and Str_3[4] == "o" and Str_3[6] == "o") or (
            Str_1[2] == "o" and Str_2[4] == "o" and Str_3[6] == "o") or (
            Str_1[2] == "o" and Str_2[2] == "o" and Str_3[2] == "o") or (
            Str_1[4] == "o" and Str_2[4] == "o" and Str_3[4] == "o") or (
            Str_1[6] == "o" and Str_2[6] == "o" and Str_3[6] == "o") or (
            Str_1[6] == "o" and Str_2[4] == "o" and Str_3[2] == "o"):
        print(Str_0 + "\n" + Str_1 + "\n" + Str_2 + "\n" + Str_3)
        result = "Поздравляю, нолики победили"
        return result
    else:
        result = "До победы ещё далеко"
        return result


Str_0 = "  0 1 2"
Str_1 = "0 - - -"
Str_2 = "1 - - -"
Str_3 = "2 - - -"
list_1 = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
while True:
    The_first_player = input("Выберите чем Вы будете играть (х/о): ")
    if The_first_player == "x":
        crosses(Str_0, Str_1, Str_2, Str_3, list_1)
        break
    elif The_first_player == "o":
        zeroes(Str_0, Str_1, Str_2, Str_3, list_1)
        break
    else:
        print("Ошибка, Вы должны были выбрать либо 'х', либо 'о'")
        continue
