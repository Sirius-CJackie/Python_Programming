# write your solution here
string = input("Write text: ")
char = string.split(' ')

correct_word = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n","")
        correct_word.append(line)

for word in char:
    if word.lower() not in correct_word:
        print(f"*{word}*", end=" ")
    else:
        print(word, end=" ")
print()