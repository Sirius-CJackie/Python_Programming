# Write your solution here
def no_vowels(string):
    vowels = 'aeiou'
    string2 = ""
    for char in string:
        if char == ' ' or char not in vowels:
            string2 += char
    return string2
    

if __name__ == "__main__":
 
    my_string = "this is an example"
    print(no_vowels(my_string))  