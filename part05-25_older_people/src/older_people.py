# Write your solution here
def older_people(people: list, year: int):
    oldest_name = []
    
    for item in people:
        if item[1] < year:

            oldest_name.append(item[0])
    return oldest_name