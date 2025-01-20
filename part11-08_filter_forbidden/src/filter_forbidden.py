# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string, forbidden):
    return ''.join([char for char in string if char not in forbidden])