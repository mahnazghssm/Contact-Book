from collections import defaultdict

class ContactBook:
    """A simple contact book application that manages contact information."""

    def __init__(self) -> None:
        # Using defaultdict to automatically create nested dictionaries
        self.contacts: dict[str, dict[str, str | None]] = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str | None = None) -> None:
        """
        Adds a new contact to the contact book.

        :param name: The name of the contact
        :param phone: The phone number of the contact
        :param email: Optional email address
        """
        if name in self.contacts:
            print("❌ Contact already exists.")
            return

        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email
        print(f"✅ Contact '{name}' added successfully.")

    def view_contact(self) -> None:
        """
        Displays all contacts in the contact book.
        """
        if not self.contacts:
            print("📭 No contacts found.")
            return

        for name, info in self.contacts.items():
            print(f"📇 Name: {name}")
            print(f"📞 Phone: {info['phone']}")
            print(f"📧 Email: {info['email']}")
            print("-" * 40)

    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact by name.

        :param name: The name of the contact to delete
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑️ Contact '{name}' deleted successfully.")
        else:
            print(f"⚠️ Contact '{name}' does not exist.")

    def update_contact(self, name: str, phone: str | None = None, email: str | None = None) -> None:
        """
        Updates a contact's phone and/or email.

        :param name: The name of the contact to update
        :param phone: New phone number (optional)
        :param email: New email address (optional)
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print("✅ Contact updated successfully.")
        else:
            print("⚠️ Contact does not exist.")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        # Display the menu
        print("\n📒 Welcome to the Contact Book Application!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contact")
        print("4. Delete Contact")
        print("5. Quit")

        # Input handling with error catch
        try:
            user_choice: int = int(input("👉 Please choose an option (1-5): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 5.")
            continue

        # Handle each menu option
        if user_choice == 5:
            print("👋 Goodbye!")
            break

        elif user_choice == 1:
            name = input("👤 Enter contact name: ")
            phone = input("📞 Enter contact phone: ")
            email = input("📧 Enter contact email (optional): ")
            book.add_contact(name, phone, email)

        elif user_choice == 2:
            name = input("👤 Enter contact name to edit: ")
            phone = input("📞 Enter new phone (leave blank to skip): ")
            email = input("📧 Enter new email (leave blank to skip): ")
            book.update_contact(name, phone or None, email or None)

        elif user_choice == 3:
            print("\n📋 List of Contacts:")
            book.view_contact()

        elif user_choice == 4:
            name = input("👤 Enter contact name to delete: ")
            book.delete_contact(name)

        else:
            print("❌ Invalid option. Please choose between 1 and 5.")