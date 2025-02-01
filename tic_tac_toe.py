"""
Tic-tac-toe game
"""


def draw_a_board(n=3):
    horizontal = ' ---'
    board = ""
    counter = 1

    for _ in range(n):
        board += "\t" + (horizontal * n) + "\n"
        board += "\t"
        for _ in range(n):
            board += f'| {counter} '
            counter += 1
        board += "|\n"

    board += "\t" + (horizontal * n)
    return board


def check_winner(board, turn):
    winning_combinations = [
        [17, 21, 25],  # Row 1 (fields 1, 2, 3)
        [46, 50, 54],  # Row 2 (fields 4, 5, 6)
        [75, 79, 83],  # Row 3 (fields 7, 8, 9)
        [17, 46, 75],  # Column 1 (fields 1, 4, 7)
        [21, 50, 79],  # Column 2 (fields 2, 5, 8)
        [25, 54, 83],  # Column 3 (fields 3, 6, 9)
        [17, 50, 83],  # Diagonal \ (fields 1, 5, 9)
        [25, 50, 75],  # Diagonal / (fields 3, 5, 7)
    ]

    for combination in winning_combinations:
        if all(board[i] == turn for i in combination):
            return True
    return False


def check_draw(board): 
    fields = [17, 21, 25, 46, 50, 54, 75, 79, 83]
    check_fields = []
    for i, field in enumerate(board):  
        if i in fields and board[i] in ['X', 'O']:
            check_fields.append(field) 

    if len(check_fields) == 9: 
        return True
    else:
        return False



def round(board, turn):
    choice = input(f'Player {turn}, pick a field: ') 
    print('\n'*10)

    board_list = list(board)

    for i, field in enumerate(board_list):
        if field == choice:  # Find the chosen field
            board_list[i] = turn  # Replace it with the player's symbol
            break  # Stop once you find and replace

    board = "".join(board_list)

    # Check for a winner
    if check_winner(board, turn):
        print(board)
        print(f'Player {turn} wins!')
        exit()  # Exit the game
    # Check for draw
    if check_draw(board): 
        print(board)
        print("Its a draw!")
        exit()

    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"

    return board, turn


def main():
    X = "X"
    O = "O"
    turn = X

    board = draw_a_board()
    print(board)
    print("We begin the game")
    while True:
        board, turn = round(board, turn)
        print(board)


main()