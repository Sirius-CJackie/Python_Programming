# Write your solution here
def count_matching_elements(list,char):
    number = 0
    for i in list:
        number += i.count(char)
    return number

if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))