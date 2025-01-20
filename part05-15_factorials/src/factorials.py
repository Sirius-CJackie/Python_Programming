def factorials(n: int):
    factorial_dict = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        factorial_dict[i] = factorial
    return factorial_dict