class NumberStats:
    def __init__(self):
        self.count = 0
        self.numbers = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.count == 0:
            return 0
        return self.numbers / self.count

def main():
    stats_even = NumberStats()  
    stats_odd = NumberStats()
    stats_all = NumberStats()   

    print("Please type in integer numbers:")
    while True:
        
        number = int(input())
        if number == -1:
            
            break
        if number % 2 == 0 or number == 1:
            stats_even.add_number(number) 
        else:
            stats_odd.add_number(number)
        stats_all
    print("Sum of numbers:", stats1.get_sum() + stats2.get_sum())
    print("Mean of numbers:", (stats1.get_sum() + stats2.get_sum()) /(stats1.count_numbers() + stats2.count_numbers()) )
    print("Sum of even numbers:", stats1.get_sum())
    print("Sum of odd numbers:", stats2.get_sum())
