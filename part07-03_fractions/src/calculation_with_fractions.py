# Write your solution here
from fractions import Fraction

def fractionate(number):
    fraction_size = Fraction(1, number)
    fractions_list = [fraction_size] * number
    return fractions_list