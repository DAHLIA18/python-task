class PhoneBook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def edit_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact {name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty. No contacts to display.")

def main():
    phone_book = PhoneBook()

    while True:
        print("\nPhone Book Application")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            phone_book.add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            phone_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter contact name to edit: ")
            new_number = input("Enter new contact number: ")
            phone_book.edit_contact(name, new_number)
        elif choice == "4":
            name = input("Enter contact name to search: ")
            phone_book.search_contact(name)
        elif choice == "5":
            phone_book.display_contacts()
        elif choice == "6":
            print("Exiting Phone Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if _name_ == "_main_":
    main()