# Write your solution here
from datetime import datetime, timedelta

def final_points():

    start_times = {}
    with open("start_times.csv", "r") as f:
        for line in f:
            name, time_str = line.strip().split(";")
            start_times[name] = datetime.strptime(time_str, "%H:%M")

    submissions = {}
    with open("submissions.csv", "r") as f:
        for line in f:
            name, task, points, time_str = line.strip().split(";")
            task = int(task)
            points = int(points)
            time = datetime.strptime(time_str, "%H:%M")
            
            if (time - start_times[name]) <= timedelta(hours=3):
                if name not in submissions:
                    submissions[name] = {}
                if task not in submissions[name] or points > submissions[name][task]:
                    submissions[name][task] = points

    total_points = {}
    for name, tasks in submissions.items():
        total_points[name] = sum(tasks.values())

    return total_points

