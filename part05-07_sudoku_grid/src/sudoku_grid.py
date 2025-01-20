def sudoku_grid_correct(sudoku: list): 
  
    for row in sudoku:
        row_list = []
        for num in row:
            if num != 0 and num in row_list:
                return False
            row_list.append(num)
    
  
    for col in range(9):
        col_list = []
        for row in range(9):
            num = sudoku[row][col]
            if num != 0 and num in col_list:
                return False
            col_list.append(num)
    
   
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            block_list = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    num = sudoku[i][j]
                    if num != 0 and num in block_list:
                        return False
                    block_list.append(num)
    
    return True
