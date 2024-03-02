from Account import Account
from Insufficient_Funds_Exception import InsufficientFundsException
from Invalid_Amount_Exception import InvalidAmountException
from Invalid_Pin_Exception import InvalidPinException


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.account_number = 1

    def register_customer(self, name, pin):
        account = Account(self.account_number, name, pin)
        self.accounts.append(account)
        self.account_number += 1
        return account

    def generate_account_number(self):
        return self.account_number

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            raise ValueError("Account not found")

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account in self.accounts:
            from_account.withdraw(amount, pin)
            to_account.deposit(amount)
        if from_account not in self.accounts:
            raise ValueError("One or both accounts not found")

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        if account:
            return account.get_balance(pin)
        else:
            raise ValueError("Account not found")

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
        else:
            raise ValueError("Account not found")

    def find_account(self, account_number) -> Account:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError("cant find account")
