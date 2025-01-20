# Write your solution here
import json
def print_persons(filename):
    with open(filename,"r") as my_file:
        data = my_file.read()
    info = json.loads(data)
    for item in info:
            name = item['name']
            age = item['age']
            if len(item['hobbies']) != 0:
                string = "("
                for hobby in item['hobbies']:
                    string += f"{hobby}, "
                string = string[:-2] 
                string += ")"
                print(f"{name} {age} years {string}")
            else:
                print(f"{name} {age} years ()")

