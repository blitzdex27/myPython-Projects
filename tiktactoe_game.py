# Tik-Tac-Toe game project from Python Bootcamp at Udemy

# Date Created: February 24, 2021
# Completion time: Around 8 hours

# import clear function
from IPython.display import clear_output

# new game

# choose piece

# game display

# game input

# check redundancy of placement input

# input process

# repeat


def new_game():
    clear_output()
    print("Welcome to Tik-Tak-Toe!")
    newgame = input("Do you want to start a new game?[Y/N]")

    if newgame == 'Y' or newgame == 'y':
        print("Great!")
        print("Mechanics:")
        print("   1. Player who choose his piece will be Player 1.")
        print("   2. Player 2 will get the piece that was not chosen.")
        print("   3. Player 1 will place his piece first.")
        print("   4. Players will put 1 piece per turn")
        print("   5. A player with a set of 3 pieces lined up will WIN!")
        print("\nGood luck!\n\n")

        return True

    elif newgame == 'n' or newgame == 'N':

        return False

    else:
        new_game()


def choose_piece():
    clear_output()
    piece_chosen = False
    invalid_token = False

    while piece_chosen is False:
        if invalid_token is True:
            print('INVALID PIECE!!')

        piece = input("Choose your piece! [X/O]")

        if piece == 'X' or piece == 'x':
            p1_piece = 'X'
            p2_piece = 'O'
            break
        elif piece == 'O' or piece == 'o':
            p1_piece = 'O'
            p2_piece = 'X'
            break
        else:
            print('Invalid piece!')
            invalid_token = True
            clear_output()

    print('3'+str(type(p1_piece)))
    return [p1_piece, 0, []], [p2_piece, 0, []]


def game_display(p1, p2):
    clear_output()

    b = [x for x in '     '*10]

    if type(p1) == list:
        for p in p1[2]:
            p = int(p)
            b[p-1] = p1[0]

        for p in p2[2]:
            p = int(p)
            b[p-1] = p2[0]

    print(f"""
    Player 1 Piece: {p1[0]}  | Player 2 Piece: {p2[0]}

    #### BOARD ######### INDEX #######
    #  {b[6] } | {b[7] } | {b[8] }   ##  [7]|[8]|[9]   #
    # ---+---+---  ##  ---+---+---   #
    #  {b[3] } | {b[4] } | {b[5] }   ##  [4]|[5]|[6]   #
    # ---+---+---  ##  ---+---+---   #
    #  {b[0] } | {b[1] } | {b[2] }   ##  [1]|[2]|[3]   #
    ##################################
    """)


def piece_placement(p1, p2):
    x = True
    while x is True:
        if p1[1] == p2[1]:
            piece = p1[2]
            piece_placement = input('Player 1:\nMove piece to: ')
            pp = int(piece_placement)
            if redundancy_test(pp, p1[2], p2[2]) is True:
                print('Invalid placement of piece!')
                pass
            else:
                p1[2].append(pp)
                p1[1] += 1
                break

        elif p1[1] > p2[1]:
            piece = p2[2]
            piece_placement = input('Player 2:\nMove piece to: ')
            pp = int(piece_placement)

            if redundancy_test(pp, p1[2], p2[2]) is True:
                print('Invalid placement of piece!')
                pass

            else:
                p2[2].append(pp)
                p2[1] += 1
                break
        else:
            continue

    game_display(p1, p2)

    p1, p2 = replaceorno(p1, p2)

    return p1, p2


def redundancy_test(piece_placement, p12, p22):
    if piece_placement in p12 or piece_placement in p22:
        return True
    else:
        return False


def input_processor(p1, p2):

    winning_combinations = [(1, 2, 3), (1, 5, 9), (1, 4, 7), (2, 5, 8),
                            (3, 5, 7), (3, 6, 9), (4, 5, 6), (7, 8, 9)]
    piece_combo = 0

    for combination in winning_combinations:

        piece_combo = 0

        for piece_placement in combination:
            if piece_placement in p1:
                piece_combo += 1
                if piece_combo == 3:
                    return 'p1'

            else:
                pass

        piece_combo = 0
        for piece_placement in combination:
            if piece_placement in p2:
                piece_combo += 1
                if piece_combo == 3:
                    return 'p2'

                else:
                    pass


def continueorno():
    con = input('\nEnter any key to continue: ')
    if con != '':
        tiktaktoe()
    else:
        pass


def replaceorno(p1, p2):
    x = True
    while x is True:
        replaceorno = input('Confirm or Replace: c/r')
        if replaceorno == 'c' or replaceorno == 'C':
            break
        elif replaceorno == 'r' or replaceorno == 'R':
            if p1[1] == p2[2]:
                p2[2].pop()
                p2[1] -= 1
                break
            else:
                p1[2].pop()
                p1[1] -= 1
                break
        else:
            print('Invalid input.')

    return p1, p2


def tiktaktoe():
    start_game = new_game()
    if start_game is True:
        p1, p2 = choose_piece()
        game_on = True
        while game_on is True:
            game_display(p1, p2)
            p1, p2 = piece_placement(p1, p2)

            win_check = input_processor(p1[2], p2[2])
            if win_check == 'p1':
                print('Player 1 WINS!')
                break
            elif win_check == 'p2':
                print('Player 2 WINS!')
                break
            else:
                pass
        continueorno()
    else:
        pass


tiktaktoe()
