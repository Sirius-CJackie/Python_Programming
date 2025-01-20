# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 == 0:
        return
    else:
        last_number = numbers[-1]
        numbers.append(last_number + 1)
        add_numbers_to_list(numbers)