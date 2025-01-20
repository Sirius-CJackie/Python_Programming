# Write your solution here
phonebook = {}

while True:

    command = input("command (1 search, 2 add, 3 quit): ")

    if command == '1':
        name = input("name: ")
        if name in phonebook:
            for item in phonebook[name]:
                print(item)
        else:
            print("no number")
    elif command == '2':
        name = input("name: ")
        number = input("number: ")
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number]
        print("ok!")
    elif command == '3':
        print("quitting...")
        break
    