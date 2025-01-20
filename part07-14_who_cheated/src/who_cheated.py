# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    # Read start times
    start_times = {}
    with open('start_times.csv', 'r') as start_file:
        start_reader = csv.reader(start_file, delimiter=';')
        for row in start_reader:
            name, time_str = row
            start_times[name] = datetime.strptime(time_str, '%H:%M')
    cheater_names = []
    with open('submissions.csv', 'r') as sub_file:
        sub_reader = csv.reader(sub_file, delimiter=';')
        for row in sub_reader:
            name, _, _, time_str = row
            submission_time = datetime.strptime(time_str, '%H:%M')
            start_time = start_times[name]
            if submission_time - start_time > timedelta(hours=3):
                if name not in cheater_names:
                    cheater_names.append(name)
    
    return cheater_names
