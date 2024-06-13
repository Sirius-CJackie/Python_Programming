# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if 0 <= index < len(my_list):
        value = int(input("New value: "))
        my_list[index] = value
        print(my_list)
    else:
        print("Invalid index. Please enter a valid index.")