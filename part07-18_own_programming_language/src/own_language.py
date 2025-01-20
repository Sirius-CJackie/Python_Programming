def find_substring_in_list(substring, lst):
    for i, string in enumerate(lst):
        if substring in string:
            return i
    return -1

def run(program):
    variables = {chr(i): 0 for i in range(65, 91)}
    output = []
    labels = {}
    i = 0
    
    while i < len(program):
        command = program[i].split()

        if command[0] == "PRINT":
            output.append(get_value(command[1], variables))
        elif command[0] == "MOV":
            variables[command[1]] = get_value(command[2], variables)
        elif command[0] == "ADD":
            variables[command[1]] += get_value(command[2], variables)
        elif command[0] == "SUB":
            variables[command[1]] -= get_value(command[2], variables)
        elif command[0] == "MUL":
            variables[command[1]] *= get_value(command[2], variables)
        elif command[0] == "JUMP":
            if find_substring_in_list(command[1], program) != -1:
                i = find_substring_in_list(command[1], program)
        elif command[0] == "IF":
            try:
                value2 = int(command[3])
                condition = get_condition(variables[command[1]], command[2], value2)
            except ValueError:
                condition = get_condition(variables[command[1]], command[2], variables[command[3]])
            if condition:
                if find_substring_in_list(command[5], program) != -1:
                    i = find_substring_in_list(command[5], program)
            else:
                i += 1  
                continue
        elif command[0] == "END":
            break
        i += 1   
    return output

def get_value(value, variables):
    if value.isdigit():
        return int(value)
    else:
        return variables[value]

def get_condition(value1, op, value2):
    if op == ">":
        return value1 > value2
    elif op == ">=":
        return value1 >= value2
    elif op == "<":
        return value1 < value2
    elif op == "<=":
        return value1 <= value2
    elif op == "==":
        return value1 == value2
    elif op == "!=":
        return value1 != value2
    return False

program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
print(result)
