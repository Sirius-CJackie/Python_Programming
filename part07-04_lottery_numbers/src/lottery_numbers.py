# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    random_numbers = sample(range(lower, upper + 1), amount)
    random_numbers.sort()

    return random_numbers

