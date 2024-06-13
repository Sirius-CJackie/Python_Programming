# Write your solution here
def store_personal_data(person):
    name , age , height = person
    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}\n")
