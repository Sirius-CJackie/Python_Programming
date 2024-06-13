# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

student = {}
exercise = {}


with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        student[parts[0]] = f"{parts[1]} {parts[2]}"

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == 'id':
            continue
        exercise_counts = [int(count) for count in parts[1:]]
        exercise[parts[0]] = sum(exercise_counts)



for student_id, total in exercise.items():
    
    print(f"{student[student_id]} {total}")