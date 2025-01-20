# Write your solution here
def block_correct(sudoku, row_no, column_no):
    seen = []
    start_row = row_no - (row_no % 3)
    start_column = column_no - (column_no % 3)
    
    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            num = sudoku[i][j]
            if num != 0 and num in seen:
                return False
            seen.append(num)
    
    return True