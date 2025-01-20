# Write your solution here
def oldest_person(people:list):
    oldest_name = ""
    oldest_year = 20000
    for item in people:
        if item[1] < oldest_year:
            oldest_year = item[1]
            oldest_name = item[0]
    return oldest_name


