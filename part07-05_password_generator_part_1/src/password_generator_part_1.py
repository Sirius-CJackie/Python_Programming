# Write your solution here
import random

def generate_password(length):
    password = ''
    for _ in range(length):
        password += random.choice('abcdefghijklmnopqrstuvwxyz')
    return password
