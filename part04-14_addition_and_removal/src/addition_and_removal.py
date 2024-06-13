# Write your solution here
list = []
i = 1
while 1:
    print(f"The list is now {list}")
    command = input("a(d)d, (r)emove or e(x)it: ")
   
    if command == 'd':
        list.append(i)
        i += 1
    elif command == 'r':
        list.pop()
        i -= 1
    elif command == 'x':
        print('Bye!')
        break