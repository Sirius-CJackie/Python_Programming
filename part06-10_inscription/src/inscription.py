# Write your solution here
user = input("Whom should I sign this to: ")
text = input("Where shall I save it: ")

with open(text,'w') as my_file:
    my_file.write(f"Hi {user}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")