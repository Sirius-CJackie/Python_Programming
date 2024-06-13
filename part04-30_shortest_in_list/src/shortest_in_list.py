# Write your solution here
def shortest(strings):
    shortest_string = strings[0]
    for string in strings[1:]:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string

if __name__ == '__main__':
    my_list1 = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list1)) 


