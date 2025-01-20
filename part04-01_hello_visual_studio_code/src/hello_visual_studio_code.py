while 1:
    name = input("Editor:")
    if name.lower() == 'visual studio code':
        print("an excellent choice!")
        break
    elif name.lower() == 'word' or name.lower() == 'notepad':
        print("awful")
    else:
        print("not good")