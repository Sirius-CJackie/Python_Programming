# Write your solution here
def row_correct(sudoku, row_no):
    seen = []
    row = sudoku[row_no]
    for item in row:
        if item != 0 and item in seen:
            return False
        seen.append(item)
    return True