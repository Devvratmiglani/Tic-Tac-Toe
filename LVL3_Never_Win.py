# <---------------Includes--------------->
# Never win
# PC will Defend Every Move You Play
# PC may not rush to win but won't let you win

import os
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

def MakeWin():
    if xo[0] == 'x' and xo[1] == 'x' and xo[2] == '-':
        xo[2] = 'o'
        return 2
    elif xo[0] == 'x' and xo[2] == 'x' and xo[1] == '-':
        xo[1] = 'o'
        return 1
    elif xo[2] == 'x' and xo[1] == 'x' and xo[0] == '-':
        xo[0] = 'o'
        return 0


    elif xo[3] == 'x' and xo[4] == 'x' and xo[5] == '-':
        xo[5] = 'o'
        return 5
    elif xo[3] == 'x' and xo[5] == 'x' and xo[4] == '-':
        xo[4] = 'o'
        return 4
    elif xo[5] == 'x' and xo[4] == 'x' and xo[3] == '-':
        xo[3] = 'o'
        return 3


    elif xo[6] == 'x' and xo[7] == 'x' and xo[8] == '-':
        xo[8] = 'o'
        return 3
    elif xo[6] == 'x' and xo[8] == 'x' and xo[7] == '-':
        xo[7] = 'o'
        return 7
    elif xo[8] == 'x' and xo[7] == 'x' and xo[6] == '-':
        xo[6] = 'o'
        return 7

#cols
    elif xo[0] == 'x' and xo[3] == 'x' and xo[6] == '-':
        xo[6] = 'o'
        return 6
    elif xo[0] == 'x' and xo[6] == 'x' and xo[3] == '-':
        xo[3] = 'o'
        return 3
    elif xo[0] == 'x' and xo[3] == 'x' and xo[6] == '-':
        xo[0] = 'o'
        return 0

    elif xo[1] == 'x' and xo[4] == 'x' and xo[7] == '-':
        xo[7] = 'o'
        return 7
    elif xo[1] == 'x' and xo[7] == 'x' and xo[4] == '-':
        xo[4] = 'o'
        return 4
    elif xo[7] == 'x' and xo[4] == 'x' and xo[1] == '-':
        xo[1] = 'o'
        return 1

    elif xo[2] == 'x' and xo[5] == 'x' and xo[8] == '-':
        xo[8] = 'o'
        return 8
    elif xo[2] == 'x' and xo[8] == 'x' and xo[5] == '-':
        xo[5] = 'o'
        return 5
    elif xo[8] == 'x' and xo[5] == 'x' and xo[2] == '-':
        xo[2] = 'o'
        return 2

#diag
    elif xo[0] == 'x' and xo[4] == 'x' and xo[8] == '-':
        xo[8] = 'o'
        return 8
    elif xo[0] == 'x' and xo[8] == 'x' and xo[4] == '-':
        xo[4] = 'o'
        return 4
    elif xo[8] == 'x' and xo[4] == 'x' and xo[0] == '-':
        xo[0] = 'o'
        return 0

    elif xo[2] == 'x' and xo[4] == 'x' and xo[6] == '-':
        xo[6] = 'o'
        return 6
    elif xo[2] == 'x' and xo[6] == 'x' and xo[4] == '-':
        xo[4] = 'o'
        return 4
    elif xo[6] == 'x' and xo[4] == 'x' and xo[2] == '-':
        xo[2] = 'o'
        return 2
    else:
        if xo[1] == '-':
            xo[1] = 'o'
            return 1
        elif xo[2] == '-':
            xo[2] = 'o'
            return 2
        elif xo[3] == '-':
            xo[3] = 'o'
            return 3
        elif xo[4] == '-':
            xo[4] = 'o'
            return 4
        elif xo[5] == '-':
            xo[5] = 'o'
            return 5
        elif xo[6] == '-':
            xo[6] = 'o'
            return 6
        elif xo[7] == '-':
            xo[7] = 'o'
            return 7
        elif xo[8] == '-':
            xo[8] = 'o'
            return 8
        elif xo[0] == '-':
            xo[0] = 'o'
            return 0
        
os.system("cls")
print("The Co-ordinate format is:")
print("0|1|2")
print("3|4|5")
print("6|7|8")

turn = 'x'
while (True):
        if turn == 'x':
            player1 = int(input("Enter PlayerX Number:"))
            if xo[player1] == '-':
                turn = 'o'
                xo[player1] = 'x'
                os.system("cls")
                if CheckWin('x'):
                    board()
                    print("Player1 wins!")
                    break
                elif '-' not in xo:
                    board()
                    print("Game Over!")
                    break
                else:
                    # sys.system("cls")
                    board()
            else:
                os.system("cls")
                board()
                print("Position Occupied")
               
        if turn == 'o':
            player2 = MakeWin()
            turn = 'x'
            #xo[player2] = 'o'
            os.system("cls")
            if CheckWin('o'):
                board()
                print("Player2 wins!")
                break
            elif '-' not in xo:
                board()
                print("Game Over!")
                break
            else:
                # sys.system("cls")
                board()
