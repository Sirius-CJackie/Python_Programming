# Write your solution here
import random
def words(n: int, beginning: str):
    with open("words.txt", "r") as file:
        words_list = [line.strip() for line in file if line[:len(beginning)] == beginning]
    if len(words_list) < n:
        raise ValueError("Not enough words starting with the specified string.")
    return random.sample(words_list, n)