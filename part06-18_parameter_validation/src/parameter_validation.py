# Write your solution here
def new_person(name: str, age: int):
    if name == '':
        raise ValueError("Name cannot be empty")
    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words")
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    
    return (name, age)