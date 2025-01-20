# Write your solution here
import re
def is_dotw(string):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun",string):
        return True
    else:
        return False

def all_vowels(string):
    for a in string:
        if re.search("[aeiouAEIOU]", a):
            continue
        else:
            return False
    return True
def time_of_day(string):
    if re.search("^([0-1][0-9]|[2][0-4]):[0-5][0-9]:[0-5][0-9]$",string):
        return True
    else:
        return False
