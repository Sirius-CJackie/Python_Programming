# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    average1 = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    average2 = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    average3 = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    
    if average1 < average2 and average1 < average3:
        return person1
    elif average2 < average1 and average2 < average3:
        return person2
    else:
        return person3