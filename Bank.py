from Account import Account


def generate_account_number(branch_code, customer_number):
    account_number_str = str(branch_code) + '{:04d}'.format(customer_number)
    return int(account_number_str)
class Bank:
    def _init_(self, name):
        self.name = name
        self.accounts = []

    def register_customer(self, name, pin):
        branch_code = 1234
        customer_number = len(self.accounts) + 1
        self.generate_account_number(branch_code, customer_number)

        account = Account()
        self.accounts.append(account)
        return account

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            raise ValueError("Account not found")

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount, pin)
        else:
            raise ValueError("Account not found")

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account:
            from_account.withdraw(amount, pin)
            to_account.deposit(amount)
        else:
            raise ValueError("One or both accounts not found")

    def check_balance(self, account_number, pin)
        account = self.find_account(account_number)
        if account:
            return account.getBalance(pin)
        else:
            raise ValueError("Account not found")

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
        else:
            raise ValueError("Account not found")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.getNumber() == account_number:
                return account
        return None

    def generate_account_number(self, branch_code, customer_number):
        pass
