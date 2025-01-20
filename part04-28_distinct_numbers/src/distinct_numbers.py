# Write your solution here
def distinct_numbers(list):
    list2 = []
    for item in list:
        if item not in list2:
            list2.append(item)
    return sorted(list2)

if __name__ == '__main__':
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
