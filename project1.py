#Project One: Connect Four

board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
columns = 7
rows = 6
def draw_field(field):
    for row in range(11):
        if row%2 == 0:
            row_number = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    column_number = int(column/2)
                    if column != 12:
                        print(field[column_number][row_number],end="")
                    else :
                        print(field[column_number][row_number])
                else:
                    print("|",end="")
        else:
            print("-------------")
def playing_board(col, player):
    column = board[col]
    index = ""
    invert_col = column[::-1]
    for row in invert_col:
        if row == " ":
            index = invert_col.index(row)
            invert_col[index] = "X" if player == 1 else "O"
            break
    if index == "":
        print("The column is full , try different column:")
        main()
    column = invert_col[::-1]
    board[col] = column
    draw_field(board)
    return True
def is_valid_location(col):
    if col >=1 and col<=7:
        return True
    else:
        return False
def winner(board, player):
# Check winner horizontally
    for c in range(columns-3):
        for r in range(rows):
            if board[c][r] == player and board[c+1][r] == player and board[c+2][r] == player and board[c+3][r] == player:
                return True
# Check winner vertically
    for c in range(columns):
        for r in range(rows-3):
            if board[c][r] == player and board[c][r+1] == player and board[c][r+2] == player and board[c][r+3] == player:
                return True
# Check winner forward diagonal
    for c in range(columns-3):
        for r in range(rows-3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
# Check winner backward diagonal
    for c in range(columns-3):
        for r in range(3, rows):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
def main():
    game_end = False
    player = 1
    while not game_end:
        if player == 1 :
            col = int(input("Player 1, select a column number from 1-7: \n"))
            if is_valid_location(col) == False:
                print('invalid move')
            else:
                playing_board(col-1,player)
                player = 2
        else:
            col = int(input("Player 2, select a column number from 1-7: \n"))
            if is_valid_location(col) == False:
                print('invalid move')
            else:
                playing_board(col-1,player)
                player = 1
        if winner(board,'X'):
            player = 1
            print("player",player,"wins")
            game_end = True
        elif winner(board,'O'):
            player = 2
            print("player",player,"wins")
            game_end = True
draw_field(board)
main()