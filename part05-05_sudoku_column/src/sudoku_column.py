# Write your solution here
def column_correct(sudoku, row_no):
    seen = []
    for item in sudoku:
        if item[row_no] != 0 and item[row_no] in seen:
            return False
        seen.append(item[row_no])
    return True