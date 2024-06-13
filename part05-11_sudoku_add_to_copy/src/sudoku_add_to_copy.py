# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print()
        for j in range(len(sudoku[i])):
            if j % 3 == 0 and j != 0:
                print(" ", end=" ")
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row[:] for row in sudoku]
    new_sudoku[row_no][column_no] = number
    return new_sudoku

