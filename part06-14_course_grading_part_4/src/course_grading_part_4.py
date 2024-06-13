# tee ratkaisu tänne
student_info = input("Student information: ")
exercises_info = input("Exercises completed: ")
exam_info = input("Exam points: ")
course_info = input("Course information: ")


students = {}
exercises = {}
exam_points = {}
exercise_points = {}
course_name = ""
course_credits = ""

with open(course_info) as course_file:
    for line in course_file:
        if line.startswith("name:"):
            course_name = line.strip().split(":")[1].strip()
        elif line.startswith("study credits:"):
            course_credits = line.strip().split(":")[1].strip()

with open(student_info) as students_file:
    for line in students_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

with open(exercises_info) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercise_counts = [int(count) for count in parts[1:]]
        total_exercises = sum(exercise_counts)
        exercises[parts[0]] = total_exercises

with open(exam_info) as exam_points_file:
    for line in exam_points_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam_counts = [int(count) for count in parts[1:]]
        total_exam_points = sum(exam_counts)
        exam_points[parts[0]] = total_exam_points

with open("results.txt", "w") as result_txt_file, open("results.csv", "w") as result_csv_file:
    result_txt_file.write(f"{course_name}, {course_credits} credits\n")
    result_txt_file.write("=" * 38 + "\n")
    result_txt_file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for student_id, total_exercises in exercises.items():
        percent_completed = total_exercises / 40 * 100
        exercise_points[student_id] = min(percent_completed // 10, 10)
    for student_id, student_name in students.items():
        exec_nbr = exercises.get(student_id, 0)
        exec_pts = int(exercise_points.get(student_id, 0))
        exm_pts = exam_points.get(student_id, 0)
        tot_pts = exec_pts + exm_pts
        if tot_pts <= 14:
            grade = 0
        elif tot_pts <= 17:
            grade = 1
        elif tot_pts <= 20:
            grade = 2
        elif tot_pts <= 23:
            grade = 3
        elif tot_pts <= 27:
            grade = 4
        else:
            grade = 5
        
        result_txt_file.write(f"{student_name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n")
        result_csv_file.write(f"{student_id};{student_name};{grade}\n")         