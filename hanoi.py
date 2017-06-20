#!/usr/bin/env python3

'''A command-line implementation of the Tower of Hanoi game.

Rates solutions based on number of moves.'''
import random
import os

from pyfiglet import figlet_format

board = [[],[],[]]
moves = 0
number_of_disks = 3 
disk_character = "#"


####################
# Set Up Interface #
####################


def clear_screen():
    '''Clears the screen.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    '''Displays the game logo.'''
    clear_screen()
    print(figlet_format('Hanoi', font='whimsy'))


def press_enter():
    '''Pauses the game until the player presses enter.'''
    input("\nPress ENTER to continue. ")


#################
# Game Specific #
#################


def finished():
    '''Checks if the game has been solved.'''
    if len(board[2]) == number_of_disks:
        return True
    return False


def new_game():
    '''Sets up a new game.'''
    global moves, board
    moves = 0
    board = [list(range(number_of_disks,0,-1)),[],[]]
    return True


def game_loop():
    '''Play the game.'''
    while not finished():
        logo()
        draw_board()
        action = input("> ").lower()
        if action == "q" or action == "quit":
            clear_screen()
            break
        elif action == "help" or action == "h":
            logo()
            print("HELP")
            print("Input the moves you'd like to make in the format below:\n\nx > y\n \nX is the column you want to take a stone from and\ny is the column you want to place it onto.\n\n2 > 1 moves the top stone from column 2 to column 1.")
            print("\nQuit exits the game and help brings up this menu.")
            press_enter()
        else:
            try:
                x, y = action.split(",")
            except ValueError:
                continue
            try:
                x = int(x.strip())
                y = int(y.strip())
            except ValueError:
                continue
            if x in range(1,4) and y in range(1,4):
                move(x, y)
    if finished():
        logo()
        draw_board()
        draw_stars(score_moves(moves,number_of_disks))
        print("Congratulations! You solved the puzzle!")
        press_enter()
    return True


def score_moves(moves, n):
    '''Calculate scores depending on the number of moves.'''
    best_moves = 2**n - 1
    stars = 1
    proportion = (moves - best_moves) / best_moves
    if proportion <= 0.2:
        stars = 3
    elif proportion <= 0.4:
        stars = 2
    return stars


def move(from_column, to_column):
    '''Moves a disk from one column to another.'''
    global board, moves
    to_column -=1
    from_column -=1
    valid = True
    if len(board[from_column]) == 0:
        valid = False
    if valid and (len(board[to_column]) == 0 or board[from_column][-1] < board[to_column][-1]):
        print("valid)")
        moves += 1
        board[to_column].append(board[from_column].pop())
    else:
        print("That is not a valid move!")
        press_enter()
        return False
    return True


########
# Menu #
########


def show_menu():
    '''Shows the game menu.'''
    while True:
        logo()
        print("Play\nHelp\nQuit")
        action = input("> ").lower()
        if action == "q" or action == "quit":
            clear_screen()
            break
        elif action == "play" or action == "p":
            new_game()
            game_loop()
        elif action == "help" or action == "h":
            draw_help()


def draw_help():
    '''Shows the help page.'''
    logo()
    print("HELP")
    print("Input the moves you'd like to make in the format below:\n\nx,y\n \nX is the column you want to take a stone from and\ny is the column you want to place it onto.\n\nExample: 2,1 moves the top stone from column 2 to column 1.")
    print("\nQUIT exits the game.\nHELP brings up this menu.")
    press_enter()


###########
# Drawing #
###########


def draw_board():
    '''Draws the game display.'''
    #print(board)
    whole = number_of_disks * 2 + 2
    mid = whole//2
    rest = whole - mid+1
    display = "=="
    for x in range(3):
        display += "="*mid + str(x+1) + "="*rest
    display += "="
    for row in range(number_of_disks+1):
        newstr = ""
        for column in range(3):
            try:
                drawing = disk_character*board[column][row]
            except IndexError:
                drawing = "|"
            else:
                drawing += "|" + drawing
            newstr += "   " + drawing.center(number_of_disks*2+1)
        display = newstr + "\n" + display
    print("Move all of the disks onto the last peg.")
    print("\n"+display)
    if not finished():
        print("\nEnter your move.\nExample:\n1, 2 moves the top disk from column 1 to column 2.\n")
        print("QUIT to quit. HELP for help")


def draw_stars(stars):
    star = [
        "    .    ",
        " __.'.__ ",
        "'-.   .-'",
        "  /.'.\  ",
        "  '   '  "
    ]
    print("")
    for line in star:
        linetext = line;
        count = stars
        while count >= 2:
            linetext += " " + line;
            count -= 1
        linetext = linetext.center(40)
        print(linetext)


###################
# Run the Program #
###################

show_menu()

