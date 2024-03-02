import unittest
from Account import Account
from Invalid_Amount_Exception import InvalidAmountException
from Invalid_Pin_Exception import InvalidPinException
#Account

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account = Account(1, "Ay", "1234")

    def test_deposit(self):
        self.account.deposit(3000)
        self.assertEqual(3000, self.account.get_balance("1234"))

    def test_twice_deposit(self):
        self.account.deposit(5000)
        self.account.deposit(4000)
        self.assertEqual(9000, self.account.get_balance("1234"))

    def test_get_account_number(self):
        self.assertEqual(1, self.account.get_account_number())

    def test_withdraw(self):
        self.account.deposit(7000)
        self.account.withdraw(5000, "1234")
        self.assertEqual(2000, self.account.get_balance("1234"))

    def test_double_withdraw(self):
        self.account.deposit(9000)
        self.account.withdraw(3000, "1234")
        self.account.withdraw(1000, "1234")
        self.assertEqual(5000, self.account.get_balance("1234"))

    def test_change_pin(self):
        self.account.change_pin("1234", "4321")
        self.assertEqual("4321", self.account.get_pin())

    def test_negative_amount(self):
        self.account = Account(1, "Blessing", "1234")
        self.assertRaises(InvalidAmountException, lambda: self.account.deposit(-300))
        self.account.deposit(2000)
        self.assertEqual(2000, self.account.get_balance("1234"))

    def test_invalid_pin(self):
        self.account = Account(1, "Samuel", "1234")
        self.account.deposit(6000)
        self.assertRaises(InvalidPinException, lambda: self.account.withdraw(2000, "2024"))


if __name__ == '__main__':
    unittest.main()
