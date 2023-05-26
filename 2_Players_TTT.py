# import os
xo = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def board():
    print(xo[0], '|', xo[1], '|', xo[2])
    print(xo[3], '|', xo[4], '|', xo[5])
    print(xo[6], '|', xo[7], '|', xo[8])


def CheckWin(checkChar):
    # rows
    if xo[0] == checkChar and xo[1] == checkChar and xo[2] == checkChar:
        return True
    if xo[3] == checkChar and xo[4] == checkChar and xo[5] == checkChar:
        return True
    if xo[6] == checkChar and xo[7] == checkChar and xo[8] == checkChar:
        return True
    # columns
    if xo[0] == checkChar and xo[3] == checkChar and xo[6] == checkChar:
        return True
    if xo[1] == checkChar and xo[4] == checkChar and xo[7] == checkChar:
        return True
    if xo[2] == checkChar and xo[5] == checkChar and xo[8] == checkChar:
        return True
    # diagonals
    if xo[0] == checkChar and xo[4] == checkChar and xo[8] == checkChar:
        return True
    if xo[2] == checkChar and xo[4] == checkChar and xo[6] == checkChar:
        return True
    return False


print("The Co-ordinate format is:")
print("0|1|2")
print("3|4|5")
print("6|7|8")

while (True):
    player1 = int(input("Enter PlayerX Number:"))
    if xo[player1] == '-':
        xo[player1] = 'x'
        # os.system("cls")
        if CheckWin('x'):
            board()
            print("Player1 wins!")
            break
        elif '-' not in xo:
            board()
            print("Game Over!")
            break
        else:
            board()
        

    player2 = int(input("Enter PlayerO Number:"))
    if xo[player2] == '-':
        xo[player2] = 'o'
        # os.system("cls")
        if CheckWin('o'):
            board()
            print("Player2 wins!")
            break
        elif '-' not in xo:
            board()
            print("Game Over!")
            break
        else:
            board()

#0 1 2 4 7 5 3 6 8 -Game Over Condition
