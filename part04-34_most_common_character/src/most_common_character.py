# Write your solution here
def most_common_character(string):
    most = 0 
    most_string = ""
    for char in string:
        count = string.count(char)
        if count > most:
            most_string = char
            most = count
        
    return most_string

if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))  # 输出: b


    
        