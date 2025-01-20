# Write your solution here
import random

def roll(die: str):
    if die == "A":
        return random.choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return random.choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return random.choice([1, 4, 4, 4, 4, 4])
def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    ties = 0
    for _ in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if result1 > result2:
            win1 += 1
        elif result2 > result1:
            win2 += 1
        else:
            ties += 1
    return (win1, win2, ties)