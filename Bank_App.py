from Bank import Bank


class BankApp:
    @staticmethod
    def enter_pin():
        return input("Enter PIN: ")

    @staticmethod
    def main():
        bank = Bank()

        try:
            while True:
                print("Welcome to DAHLIA'S Bank")
                print("Select an option:")
                print("1. Register Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Check Balance")
                print("6. Remove Account")
                print("7. Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    name = input("Enter name: ")
                    pin = BankApp.enter_pin()
                    bank.register_customer(name, pin)
                    print("Account registered successfully.")
                elif choice == 2:
                    account_number = int(input("Enter account number: "))
                    deposit_amount = float(input("Enter amount to deposit: "))
                    bank.deposit(account_number, deposit_amount)
                    print("Deposit successful.")
                elif choice == 3:
                    account_number = int(input("Enter account number: "))
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                    withdraw_pin = BankApp.enter_pin()
                    bank.withdraw(account_number, withdraw_amount, withdraw_pin)
                    print("Withdrawal successful.")
                elif choice == 4:
                    from_account_number = int(input("Enter account number to transfer from: "))
                    to_account_number = int(input("Enter account number to transfer to: "))
                    transfer_amount = float(input("Enter amount to transfer: "))
                    transfer_pin = BankApp.enter_pin()
                    bank.transfer(from_account_number, to_account_number, transfer_amount, transfer_pin)
                    print("Transfer successful.")
                elif choice == 5:
                    account_number = int(input("Enter account number: "))
                    check_balance_pin = BankApp.enter_pin()
                    balance = bank.check_balance(account_number, check_balance_pin)
                    print("Current balance:", balance)
                elif choice == 6:
                    account_number = int(input("Enter account number: "))
                    remove_account_pin = BankApp.enter_pin()
                    bank.remove_account(account_number, remove_account_pin)
                    print("Account removed successfully.")
                elif choice == 7:
                    print("Thank you for using DAHLIA'S Bank. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)

        finally:
            pass


if __name__ == "_main_":
    BankApp.main()
