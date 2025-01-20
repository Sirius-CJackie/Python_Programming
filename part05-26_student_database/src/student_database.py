# Write your solution here

def  add_student(students: dict, name: str):
    students[name]= []
   
def print_student(students: dict, name: str):
    total = 0
    if name in students:
        print(name+":")
        if students[name] == []:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
                total += course[1]
            average = total/len(students[name])
            print(f" average grade {average}")
            
                
    else:
       
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str,courses:tuple):
    if name in students:
        course_name, grade = courses
        found = False
        for i in range(len(students[name])):
            existing_course, existing_grade = students[name][i]
            if existing_course == course_name:
                if grade > existing_grade:
                    students[name][i] = (course_name, grade)
                found = True
                break
        if not found and grade > 0:
            students[name].append(courses)
            

def summary(students: dict):
    total_students = len(students)
    max_courses_completed = 0
    total = 0
    average = 0
    best_average_grade = 0
    best_student = ""
    most_student = ""
    
    for student, courses in students.items():
        num_courses_completed = len(courses)
        if num_courses_completed > max_courses_completed:
            max_courses_completed = num_courses_completed
            most_student = student
        for i in courses:
            total += i[1]
        average = total/len(courses)
        if average > best_average_grade: 
            best_average_grade = average
            best_student = student        
        
             
            
    print(f"students {total_students}")
    print(f"most courses completed {max_courses_completed} {most_student}")
    print(f"best average grade {best_average_grade} {best_student}")
