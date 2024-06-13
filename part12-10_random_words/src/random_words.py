# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        word = ''.join(random.choices(characters, k=length))
        yield word