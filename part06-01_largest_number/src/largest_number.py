# write your solution here
def largest():    
    with open("numbers.txt") as file:
        largest = 0
        for line in file:
            number = int(line)
            if number > largest:
                largest = number
    
    return largest
                
                


