# Write your solution here
with open("diary.txt", "a+") as file:
    file.seek(0)
    entries = file.readlines()

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")

    if function == '1':
        new_entry = input("Diary entry: ")
        entries.append(new_entry + "\n")
        with open("diary.txt", "w") as file:
            file.writelines(entries)
        print("Diary saved")
    elif function == '2':
        print("Entries:")
        for entry in entries:
            print(f"{entry.strip()}")
    elif function == '0':
        print("Bye now!")
        break

