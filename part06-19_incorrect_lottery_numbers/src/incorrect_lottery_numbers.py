# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv", "r") as old_file, open("correct_numbers.csv", "w") as new_file:
        for line in old_file:
            parts = line.strip().split(';')
            try:
                week = int(parts[0][5:])  
                if week < 1:
                    raise ValueError("Invalid week number")
                numbers = [int(num) for num in parts[1].split(',')]  # Extracting the numbers
                if len(numbers) != 7:
                    raise ValueError("Incorrect number of lottery numbers")
                if any(num < 1 or num > 39 for num in numbers):
                    raise ValueError("Numbers out of range")
                for i in range(len(numbers)):
                    for j in range(i + 1, len(numbers)):
                        if numbers[i] == numbers[j]:
                            raise ValueError("Duplicate numbers found")
                
                new_file.write(line)
                
            except (ValueError, IndexError):
                continue

