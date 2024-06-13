# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

millennium = datetime(1999,12,31)
bron = datetime(year,month,day)
if bron < millennium:
    days = millennium - bron
   
    print(f"You were {days.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")