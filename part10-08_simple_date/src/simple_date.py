# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day_param, month_param, year_param):
        self.__day = day_param
        self.__month = month_param
        self.__year = year_param
    
    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'
    
    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month < other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day < other.__day:
                    return True

        return False

    def __gt__(self, other):
        if not self.__eq__(other) and not self.__lt__(other):
            return True
        return False

    def __eq__(self, other):
        if self.__day == other.__day and \
            self.__month == other.__month and \
                self.__year == other.__year:
                return True
        return False

    def __ne__(self, other):
        if not self.__eq__(other):
            return True
        return False

    def __convert_curr_date_to_days(self):
        return ((self.__year-1)*12*30) + ((self.__month-1)*30) + self.__day

    def __add__(self, days_to_add):
        days = self.__convert_curr_date_to_days()
        days += days_to_add
        year = (days//360)+1
        month = ((days//30)%12)+1
        day = days%30
        return SimpleDate(day, month, year)

    def __sub__(self, other):
        curr_days = self.__convert_curr_date_to_days()
        other_days = other.__convert_curr_date_to_days()
        return abs(curr_days - other_days)

