# Write your solution here
def search_by_name(filename, word):
    recipes_name = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            for char in line:
                if char.isupper():
                    if word.lower() in line.lower():
                        recipes_name.append(line)
                
    return recipes_name

def search_by_time(filename, time):
    recipes_name = []
    pre_line = ""
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                if int(line) <= time:
                    recipes_name.append(f"{pre_line}, preparation time {line} min")
            else:
                pre_line = line
    return recipes_name

def search_by_ingredient(filename, ingredient):
    recipes = []
    recipes_name = []
    pre_message = []
    with open(filename) as file:
        for line in file:
            if line != '\n':
                pre_message.append(line.strip())
            else:
                recipes_name.append(pre_message)
                pre_message = []
        if pre_message:
            recipes_name.append(pre_message)

        for recipe in recipes_name:
            if ingredient in recipe:
                recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
        return recipes



