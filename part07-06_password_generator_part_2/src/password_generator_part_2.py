# Write your solution here
import random

def generate_strong_password(length, include_digits=True, include_special_chars=True):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_chars = '!?=+-()#'
    password = random.choice(lowercase_letters)
    if include_digits:
        password += random.choice(digits)
    if include_special_chars:
        password += random.choice(special_chars)
    remaining_length = length - len(password)
    all_chars = lowercase_letters
    if include_digits:
        all_chars += digits
    if include_special_chars:
        all_chars += special_chars
    for _ in range(remaining_length):
        password += random.choice(all_chars)
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''
    for char in password_list:
        shuffled_password += char

    return shuffled_password