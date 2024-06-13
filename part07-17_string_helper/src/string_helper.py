# Write your solution here
def change_case(orig_string: str) -> str:
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple:
    length = len(orig_string)
    half_length = length // 2
  
    part1 = orig_string[:half_length]
    part2 = orig_string[half_length:]
  
    return part1, part2


def remove_special_characters(orig_string: str) -> str:
    new_string = ''
    for c in orig_string:
        if c.isalnum() or c.isspace():
            new_string += c
    return new_string