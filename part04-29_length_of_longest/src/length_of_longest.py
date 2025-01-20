# Write your solution here
def length_of_longest(string_list):
    if not string_list:
        return 0
    best = len(string_list[0])
    for string in string_list:
        if len(string) > best:
            best = len(string)
    return best
if __name__ == "__main__":
    my_list1 = ["first", "second", "fourth", "eleventh"]
    result1 = length_of_longest(my_list1)
    print(result1)  

    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result2 = length_of_longest(my_list2)
    print(result2)  