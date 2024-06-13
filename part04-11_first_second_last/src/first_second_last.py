# Write your solution here
# You can test your function by calling it within the following block
def first_word(string):
    index = string.find(" ")
    return string[0:index]

def second_word(string):
    index = string.find(" ")
    index2 = string[index+1:].find(" ")

    if index2 != -1:
        return string[index+1:index2+index+1]
    else: 
        return string[index+1:]
def last_word(string):
    index = string.rfind(" ")
    return string[index+1:]

if __name__ == "__main__":
    sentence = "frist second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))