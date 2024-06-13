class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts):
    return list(filter(lambda x: x.grade>=1,attempts))
def attempts_with_grade(attempts, grade):
    return list(filter(lambda x: x.grade==grade,attempts))
def passed_students(attempts, course):
    return sorted(map(lambda y: y.student_name,list(filter(lambda x: x.grade>=1,filter(lambda x: x.course_name == course, attempts)))))


