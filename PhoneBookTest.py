import unittest
from phonebook import PhoneBook

class Test_Phone_Book(unittest.TestCase):
    def setUp(self):
        self.phone_book = PhoneBook()

    def test_add_contact(self):
        self.phone_book.add_contact("Dahlia", "1234567890")
        self.assertIn("Dahlia", self.phone_book.contacts)
        self.assertEqual(self.phone_book.contacts["Dahlia"], "1234567890")

    def test_delete_contact(self):
        self.phone_book.add_contact("Bobby", "9876543210")
        self.phone_book.delete_contact("Bobby")
        self.assertNotIn("Bobby", self.phone_book.contacts)

    def test_edit_contact(self):
        self.phone_book.add_contact("Charles", "4567890123")
        self.phone_book.edit_contact("Charles", "1112223333")
        self.assertEqual(self.phone_book.contacts["Charles"], "1112223333")

    def test_search_contact_found(self):
        self.phone_book.add_contact("David", "4445556666")
        self.assertTrue(self.phone_book.search_contact("David"))

    def test_search_contact_not_found(self):
        self.assertFalse(self.phone_book.search_contact("Eve"))


if __name__ == "_main_":
    unittest.main()
