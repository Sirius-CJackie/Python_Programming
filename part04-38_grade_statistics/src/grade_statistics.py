# Write your solution here


def passed_exam(exam):
    return exam >= 10

def statistics(total,grade):
    while 1:
        total_grade = 0
        string = input("Exam points and exercises completed: ")
        if not string:
                break
        exam,exercise = string.split()
        exam = int(exam)
        exercise = int(exercise)
        total_grade = exam + exercise//10
        total += total_grade

        if passed_exam(exam) == False:
            grade[0] += 1
        else:
            if total_grade < 15:
                 grade[0] += 1
            elif total_grade < 18:
                 grade[1] += 1
            elif total_grade < 21:
                 grade[2] += 1
            elif total_grade < 24:
                 grade[3] += 1
            elif total_grade < 28:
                 grade[4] += 1
            else:
                 grade[5] += 1  
    return total

def print_statistics(total,grade):
    if sum(grade) == 0:
        return
    average = total / sum(grade)

    pass_percentage = (1 - grade[0] / sum(grade)) * 100
    print("Statistics:")
    print("Points average: {:.1f}".format(average))
    print("Pass percentage: {:.1f}".format(pass_percentage))
    print("Grade distribution:")
    print("  5: "+"*"*grade[5])
    print("  4: "+"*"*grade[4])
    print("  3: "+"*"*grade[3])
    print("  2: "+"*"*grade[2])
    print("  1: "+"*"*grade[1])
    print("  0: "+"*"*grade[0])


def main():
    total = 0
    grade = [0,0,0,0,0,0]
    
    print_statistics(statistics(total,grade),grade)

main()