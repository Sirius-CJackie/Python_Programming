# Write your solution here
layers = int(input("Layers: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(layers):
    for j in range(layers):
        print(alphabet[layers - 1 - min(i, j)], end="")
    for j in range(layers - 2, -1, -1):
        print(alphabet[layers - 1 - min(i, j)], end="")
    print()
for i in range(layers - 2, -1, -1):
    for j in range(layers):
        print(alphabet[layers - 1 - min(i, j)], end="")
    for j in range(layers - 2, -1, -1):
        print(alphabet[layers - 1 - min(i, j)], end="")
    print()