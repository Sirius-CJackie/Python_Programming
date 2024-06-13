# Write your solution here
def everything_reversed(list):
    index = len(list) - 1
    list2 = []
    while index >= 0:
        list2.append(list[index][::-1])
        index -= 1
    return list2
if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
