# Write your solution here
import json
import urllib.request

import json
import urllib.request

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    
    active_courses = []
    for course in data:
        if course['enabled']:
            active_courses.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
    return active_courses

def retrieve_course(course_name):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
   
    weeks = len(data)
    
    students = max([data[str(week)]['students'] for week in data]) if data else 0
    hours = sum([data[str(week)]['hour_total'] for week in data]) if data else 0
    exercises = sum([data[str(week)]['exercise_total'] for week in data]) if data else 0


    return {
        'weeks': weeks,
        'students': students,
        'hours': hours,
        'hours_average': hours // students,
        'exercises': exercises,
        'exercises_average': exercises // students
    }




