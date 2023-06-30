
rules = """"
\t\t\t\t---------Welcome to Tic Tac Toe game---------\t\t\t\t

\t\t\t\tPlayer 1: X \t\t Player 2: O


1)Player should pick a number between 1 to 9 which will determine your position of X/O
2)Player should not enter anything other than numbers.
3)For placing X/O in the position you want here is an example

 1 | 2 | 3 
---+---+----
 4 | 5 | 6 
---+---+----
 7 | 8 | 9 

when asked where do you want to place X/O press the corresponding place number i.e in this example lets say we place X on 5th position
your output will be:

 1 | 2 | 3 
---+---+----
 4 | X | 6 
---+---+----
 7 | 8 | 9  
\t\t----------------------------------------------X----------------------------------------------  
"""

X_and_O = ["1","2","3","4","5","6","7","8","9"]

def print_board():
    print()
    print(f" {X_and_O[0]} | {X_and_O[1]} | {X_and_O[2]} ")
    print("---+---+----")
    print(f" {X_and_O[3]} | {X_and_O[4]} | {X_and_O[5]} ")
    print("---+---+----")
    print(f" {X_and_O[6]} | {X_and_O[7]} | {X_and_O[8]} ")
    print()



def player1():
    player1_X = int(input("Enter the position you want to write X(Player 1): "))
    if player1_X >=1 and player1_X <= 9:
        if X_and_O[player1_X - 1] in ["1","2","3","4","5","6","7","8","9"]:
            X_and_O[player1_X - 1] ="X"
            print_board()
        else:
            print("That spot is already taken")
            print()
            player1()
    else:
        print("Enter a valid number between 1 and 9")
        print()
        player1()
        

def player2():
    player2_O = int(input("Enter the position you want to write O(Player 2): "))
    if player2_O >=1 and player2_O <= 9:
        if X_and_O[player2_O - 1] in ["1","2","3","4","5","6","7","8","9"]:
            X_and_O[player2_O - 1] ="O"
            print_board()
        else:
            print("This spot is aready taken,Enter a valid spot")
            print()
            player2()
    else:
        print("Enter a valid number between 1 and 9")
        print()
        player2()

def win():
    if X_and_O[0] == X_and_O[1] == X_and_O[2] == "X" or X_and_O[3] == X_and_O[4] == X_and_O[5] ==  "X" or X_and_O[6] == X_and_O[7] == X_and_O[8] == "X":
        return "Player 1 won"
    elif  X_and_O[0] == X_and_O[1] == X_and_O[2] == "O" or X_and_O[3] == X_and_O[4] == X_and_O[5] ==  "O" or X_and_O[6] == X_and_O[7] == X_and_O[8] == "O":
        return "Player 2 won"
    elif X_and_O[0] == X_and_O[3] == X_and_O[6] == "X" or X_and_O[1] == X_and_O[4] == X_and_O[7] == "X"  or X_and_O[2] == X_and_O[5] == X_and_O[8] == "X":
        return "Player 1 won"
    elif X_and_O[0] == X_and_O[3] == X_and_O[6] == "O" or X_and_O[1] == X_and_O[4] == X_and_O[7] == "O"  or X_and_O[2] == X_and_O[5] == X_and_O[8] == "O":
        return "Player 2 won" 
    elif X_and_O[0] == X_and_O[4] == X_and_O[8] == "X"  or X_and_O[2] == X_and_O[4] == X_and_O[6] == "X":
        return "Player 1 won"
    elif X_and_O[0] == X_and_O[4] == X_and_O[8] == "O"  or X_and_O[2] == X_and_O[4] == X_and_O[6] == "O":
        return "Player 2 won"
    elif (X_and_O[0] != "1" and X_and_O[1] != "2" and X_and_O[2] != "3" and X_and_O[3] != "4" and X_and_O[4] != "5" and X_and_O[5] != "6" and X_and_O[6] != "7" and X_and_O[7] != "8" and X_and_O[8] != "9"):
        return "Game tied"
    else:
        pass

def win_checker(func):
    if func == "Player 1 won":
        print("Player 1 won")
        return "break"
    elif func == "Player 2 won":
        print("Player 2 won")
        return "break"
    elif func == "Game tied":
        print("Game is tied")
        return "break"
    else:
        pass
    
if __name__ == "__main__":
    print(rules,end = "\n\n\n")
    print_board()
    while True:
        player1()
        print("\033[H\033[J")
        print_board()
        if win_checker(win()) == "break":
            break
        player2()
        print("\033[H\033[J")
        print_board()
        if win_checker(win()) == "break":
            break
            

    
        
