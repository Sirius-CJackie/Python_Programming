# Write your solution here
import string
def separate_characters(mystring):
    know = ''
    punctuation = ''
    unknow = ''
    for char in mystring:
        if char in string.ascii_letters:
            know += char
        elif char in string.punctuation:
            punctuation += char
        else:
            unknow += char
    
    # Return the three strings as a tuple
    return know, punctuation, unknow