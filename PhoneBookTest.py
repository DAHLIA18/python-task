import unittest
from unittest.mock import patch
from io import StringIO

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = PhoneBook()

    def test_add_contact(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.add_contact("Dahlia", "123-456-7890")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact Dahlia added successfully.")

    def test_delete_contact(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.delete_contact("NonExistentContact")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact NonExistentContact not found.")

        self.phone_book.add_contact("Alice", "111-222-3333")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.delete_contact("Alice")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact Alice deleted successfully.")

    def test_edit_contact(self):
        self.phone_book.add_contact("Bob", "999-888-7777")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.edit_contact("Bob", "555-666-4444")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact Bob updated successfully.")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.edit_contact("NonExistentContact", "123-456-7890")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact NonExistentContact not found.")

    def test_search_contact(self):
        self.phone_book.add_contact("Charlie", "777-888-9999")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.search_contact("Charlie")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact Charlie: 777-888-9999")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.search_contact("NonExistentContact")
            self.assertEqual(mock_stdout.getvalue().strip(), "Contact NonExistentContact not found.")

    def test_display_contacts(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.display_contacts()
            self.assertEqual(mock_stdout.getvalue().strip(), "Phone book is empty. No contacts to display.")

        self.phone_book.add_contact("David", "444-555-6666")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.phone_book.display_contacts()
            expected_output = "Contacts:\nDavid: 444-555-6666"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if _name_ == '_main_':
    unittest.main()