# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date = input("Starting date (dd.mm.yyyy): ")
num_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
start_date_obj = datetime.strptime(starting_date, "%d.%m.%Y")
end_date_obj = start_date_obj + timedelta(days=num_days - 1)

with open(filename, "w") as file:
    file.write(f"Time period: {start_date_obj.strftime('%d.%m.%Y')}-{end_date_obj.strftime('%d.%m.%Y')}\n")
    
    total_minutes = 0
    screen_time_data = []
    for i in range(num_days):
        date = input(f"Screen time {start_date_obj.strftime('%d.%m.%Y')}: ")
        screen_time = [int(time) for time in date.split()]
        total_minutes += sum(screen_time)
        screen_time_data.append(f"{start_date_obj.strftime('%d.%m.%Y')}: {screen_time[0]}/{screen_time[1]}/{screen_time[2]}")
        start_date_obj += timedelta(days=1)
    
    file.write("Total minutes: " + str(total_minutes) + "\n")
    file.write("Average minutes: " + str(total_minutes / num_days) + "\n")
    for data in screen_time_data:
        file.write(data + "\n")

print(f"Data stored in file {filename}")