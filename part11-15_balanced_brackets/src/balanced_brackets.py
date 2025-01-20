def balanced_brackets(my_string):
    my_string = ''.join([character for character in my_string if character in '()[]'])
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False
    return balanced_brackets(my_string[1:-1])

