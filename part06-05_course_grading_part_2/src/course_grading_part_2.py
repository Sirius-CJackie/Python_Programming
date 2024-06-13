# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points_data = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points_data = "exam_points1.csv"

students = {}
exercises = {}
exam_points = {}
exercise_points = {}

with open(student_info) as students_file:
    for line in students_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

with open(exercise_data) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercise_counts = [int(count) for count in parts[1:]]
        total_exercises = sum(exercise_counts)
        exercises[parts[0]] = total_exercises

with open(exam_points_data) as exam_points_file:
    for line in exam_points_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam_counts = [int(count) for count in parts[1:]]
        total_exam_points = sum(exam_counts)
        exam_points[parts[0]] = total_exam_points


for student_id, total_exercises in exercises.items():
    percent_completed = total_exercises / 40 * 100
    exercise_points[student_id] = min(percent_completed // 10, 10)

for student_id, student_name in students.items():
    total_points = exam_points.get(student_id, 0) + exercise_points.get(student_id, 0)
    if total_points <= 14:
        grade = 0
    elif total_points <= 17:
        grade = 1
    elif total_points <= 20:
        grade = 2
    elif total_points <= 23:
        grade = 3
    elif total_points <= 27:
        grade = 4
    else:
        grade = 5
    print(f"{student_name} {grade}")
