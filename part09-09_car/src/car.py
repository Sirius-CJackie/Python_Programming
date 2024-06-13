# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol_level = 0  
        self.__odometer_reading = 0  
    def fill_up(self):
        if self.__petrol_level < 60:
            self.__petrol_level = 60 
    def drive(self, km):
        petrol_needed = km 
        if petrol_needed > self.__petrol_level: 
            km_driven = self.__petrol_level
            self.__petrol_level = 0
        else:
            km_driven = petrol_needed
            self.__petrol_level -= petrol_needed
        self.__odometer_reading += km_driven

    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__petrol_level} litres"
