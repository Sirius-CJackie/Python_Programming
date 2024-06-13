# Write your solution here
while 1:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == '1':
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish_word} - {english_word}\n")
        print("Dictionary entry added")
    elif choice == '2':
        search_term = input("Search term: ")
        with open("dictionary.txt", "r") as file:
            for line in file:
                finnish, english = line.strip().split(" - ")
                if search_term.lower() == english.lower() or search_term.lower() == finnish.lower() or search_term.lower() in english.lower() or search_term.lower() in finnish.lower():
                    print(f"{finnish} - {english}")
    elif choice == '3':
        print("Bye!")
        break