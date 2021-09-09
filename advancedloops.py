#Homework #6: Advanced Loops
import shutil

size = shutil.get_terminal_size()
Width = size.columns
Height = size.lines


def gameBoard(row, column):
    if(column>Height or row>Width):
        return False
    else:
        for r in range (row):
            for c in range(column+1):
                print("| ", end="")
            print()
            print("-"*column*2)
        return True

gameBoard(25, 20)
