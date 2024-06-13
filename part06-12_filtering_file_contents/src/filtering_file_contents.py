# Write your solution here
def filter_solutions():
    with open("solutions.csv", "r") as file:
        correct_file = open("correct.csv", "w")
        incorrect_file = open("incorrect.csv", "w")
        for line in file:
            name, problem, result = line.strip().split(";")
            if eval(problem) == int(result):
                correct_file.write(line)
            else:
                incorrect_file.write(line)
        correct_file.close()
        incorrect_file.close()

