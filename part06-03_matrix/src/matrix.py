# write your solution here
def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            row = [int(x) for x in line.strip().split(",")]
            matrix.append(row)
    return matrix

def matrix_sum():
    matrix = read_matrix()
    total_sum = sum(sum(row) for row in matrix)
    return total_sum

def matrix_max():
    matrix = read_matrix()
    max_element = max(max(row) for row in matrix)
    return max_element

def row_sums():
    matrix = read_matrix()
    sums = [sum(row) for row in matrix]
    return sums