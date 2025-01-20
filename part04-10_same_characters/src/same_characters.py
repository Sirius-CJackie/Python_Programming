# Write your solution here
# You can test your function by calling it within the following block
def same_chars(string,x,y):
    if x <= len(string)-1  and y <= len(string)-1:
        if string[x] == string[y]:
            return True
        else:
            return False
    else: 
        return False



if __name__ == "__main__":
    print(same_chars("coder", 1, 2))