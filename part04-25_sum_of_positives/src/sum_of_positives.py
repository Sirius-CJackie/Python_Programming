# Write your solution here
def sum_of_positives(list):
    list2 =[]
    for item in list:
        if item > 0:
            list2.append(item)
        
            
    return sum(list2)




if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)