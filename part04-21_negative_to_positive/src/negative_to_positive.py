# Write your solution here
N = int(input("Please type in a positive integer: "))

# Print numbers between -N and N inclusive, excluding 0
for i in range(-N, N + 1):
    if i != 0:
        print(i)