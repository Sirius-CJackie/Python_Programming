# Write your solution here
def find_words(search_term):
    with open("words.txt") as file:
        words = file.read().splitlines()

    matches = []

    if '*' in search_term:
        if search_term.startswith('*'):
            prefix = search_term[1:]
            matches = [word for word in words if word.endswith(prefix)]
        elif search_term.endswith('*'):
            suffix = search_term[:-1]
            matches = [word for word in words if word.startswith(suffix)]
        else:
            prefix, suffix = search_term.split('*')
            matches = [word for word in words if word.startswith(prefix) and word.endswith(suffix)]
    elif '.' in search_term:
        pattern = search_term.replace('.', '.')
        matches = [word for word in words if len(word) == len(pattern) and all(a == b or b == '.' for a, b in zip(word, pattern))]
    else:
        matches = [word for word in words if word == search_term]

    return matches