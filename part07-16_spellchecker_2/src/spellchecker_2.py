# Write your solution here
from difflib import get_close_matches

def spell_checker(text, word_list):
    def process_word(word):
        suggestions = get_close_matches(word, word_list)
        if suggestions:
            suggestions_str = ""
            for suggestion in suggestions:
                suggestions_str += suggestion + ", "
            return f"*{word}*", suggestions_str
        else:
            return word,""

    corrected_text = ""
    suggestions_text = "suggestions:\n"
    for word in text.split():
        if word.lower() not in word_list:
            corrected_word , suggestions= process_word(word)
            corrected_text += corrected_word + " "
            if "*" in corrected_word:
                suggestions_text += f"{corrected_word.split('*')[1].strip()}: {suggestions}\n"


        else:
            corrected_text += word + " "

    return corrected_text.strip(), suggestions_text.strip()

with open("wordlist.txt", "r") as file:
    word_list = set(file.read().splitlines())

user_input = input("write text: ")
corrected_text, suggestions_text = spell_checker(user_input, word_list)
print(corrected_text)
if suggestions_text:
    print(suggestions_text)