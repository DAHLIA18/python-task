from Insufficient_Funds_Exception import InsufficientFundsException
from Invalid_Amount_Exception import InvalidAmountException
from Invalid_Pin_Exception import InvalidPinException


class Account:

    def __init__(self, number, name, pin):
        self.number = number
        self.name = name
        self.pin = pin
        self.balance = 0.0

    def get_account_number(self):
        return self.number

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("please try again")
        self.balance += amount

    def withdraw(self, amount, pin) -> float:
        if amount <= 0:
            raise InsufficientFundsException("please try a positive amount")
        if pin != self.pin:
            raise InvalidPinException("Incorrect pin")
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise InvalidPinException("Incorrect PIN")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
        else:
            raise ValueError("Incorrect old PIN")

    def get_pin(self):
        return self.pin

    def __repr__(self):
        return f"{self.number}"
