from Insufficient_Funds_Exception import InsufficientFundsException
from Invalid_Amount_Exception import InvalidAmountException
from Invalid_Pin_Exception import InvalidPinException


class BankAccount:

    def __init__(self):
        self.pin = None
        self.number = None
        self.balance = None
        self.name = None

    def _init_(self, number, name, pin, balance=0):
        self.number = number
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("try again")
        self.balance += amount

    def withdraw(self, amount, pin):
        self.check_pin(pin)
        if amount <= 0:
            raise InvalidAmountException("try again")
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficient funds")

    def check_balance(self, pin):
        if self.check_pin(pin):
            return self.balance

    def check_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinException("Invalid pin")

    def change_pin(self, old_pin, new_pin):
        self.check_pin(old_pin)
        self.pin = new_pin

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def init(self, param, param1, param2, param3):
        pass
