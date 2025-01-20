# Write your solution here:
class Person:

    def __init__(self,full_name):
        self.full_name = full_name


    def return_first_name(self):
        parts = self.full_name.split(" ")
        return parts[0]
    
    def return_last_name(self):
        parts = self.full_name.split(" ")
        return parts[1]













