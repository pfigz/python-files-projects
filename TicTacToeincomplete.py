#Tic Tac Toe

# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#01234


def draw_field(field):
    for row in range(5):  #0,1,2,3,4
                          #0,.,1,.,2
        if row%2 == 0:
            practical_row = int(row/2)
            for column in range(5): #01234
                if column%2 == 0:
                    practical_column = int(column/2)
                    if column != 4:
                        print(field[practical_column][practical_row],end = "")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|",end = "")
        else:
            print("-----")

Player = 1
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_field(current_field)
while True:
    print("Players turn:", Player)
    move_row = int(input("Please enter the row\n"))
    move_column = int(input("Please enter the column\n"))
    if Player == 1:
        #move for player 1
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "X"
            Player = 2
    else:
        #move for player 2
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "O"
            Player = 1
    draw_field(current_field)
