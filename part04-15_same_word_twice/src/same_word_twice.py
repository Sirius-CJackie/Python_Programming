# Write your solution here
list = []
while 1:
    word = input("Word: ")
    if word in list :
        break
    else:
        list.append(word)
print(f"You typed in {len(list)} different words")