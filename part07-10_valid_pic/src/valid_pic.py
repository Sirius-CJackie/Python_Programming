# Write your solution here
from datetime import datetime
import calendar

def is_valid_date(dob,century_marker):
    day = int(dob[:2])
    month = int(dob[2:4])
    year = int(dob[4:])
    
    if century_marker == '+':
        year += 1800 
    elif century_marker == '-':
        year += 1900 
    elif century_marker == 'A':
        year += 2000
   
    if month < 1 or month > 12:
        return False
    
    if month in [4, 6, 9, 11]:
        
        if day < 1 or day > 30:
            return False
    elif month == 2:
        
        if calendar.isleap(year):
            if day < 1 or day > 29:
                return False
        elif day < 1 or day > 28:
            return False
    elif month in [1,3,5,7,8,10,12]:
       
        if day < 1 or day > 31:
            return False
    
    return True


def is_it_valid(pic):
    if len(pic) != 11:
        return False
    dob = pic[:6]
    century_marker = pic[6]
    personal_id = pic[7:10]
    control_character = pic[10]
    
    if not is_valid_date(dob,century_marker):
        return False
    if century_marker not in ['+', '-', 'A']:
        return False
    dob_personal_id = dob + personal_id
    control_index = int(dob_personal_id) % 31
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXYC"
    calculated_control_character = control_chars[control_index]
    return control_character == calculated_control_character



