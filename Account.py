class Account:
    def _init_(self, number, name, pin):
        self.number = number
        self.name = name
        self.pin = pin
        self.balance = 0.0

    def getNumber(self):
        return self.number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if self.pin == pin:
            self.balance -= amount
        else:
            raise ValueError("Incorrect PIN")

    def getBalance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise ValueError("Incorrect PIN")

    def changePin(self, oldPin, newPin):
        if self.pin == oldPin:
            self.pin = newPin
        else:
            raise ValueError("Incorrect old PIN")