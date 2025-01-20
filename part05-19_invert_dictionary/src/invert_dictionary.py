# Write your solution here
def invert(dictionary: dict):
    inverted_dict={}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    dictionary.clear()
    for key, value in inverted_dict.items():
        dictionary[key] = value 
        
