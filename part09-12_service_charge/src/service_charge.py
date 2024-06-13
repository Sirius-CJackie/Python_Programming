# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
    def __service_charge(self):
        self.__balance -= 0.01 * self.__balance
    def deposit(self, amount):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount):
        self.__balance -= amount
        self.__service_charge()
    @property
    def balance(self):
        return self.__balance


