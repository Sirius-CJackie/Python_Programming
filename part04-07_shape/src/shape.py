# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def drew(size,string):
    print(string*size)


def shape(tri,string1,squ,string2):
    for i in range(tri):
        drew(i+1,string1) 
    for i in range(squ):
        drew(tri,string2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")