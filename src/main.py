 from collections import defaultdict

# Define the ContactBook class
class ContactBook:
    # Constructor method for initializing the contact book
    def __init__(self):
        # Type: contact -> defaultdict[str, dict]
        # Using defaultdict to store contacts, where each key is a name (string)
        # and the value is a dictionary containing 'phone' and 'email'
        self.contact = defaultdict(dict)

    # Method to add a contact to the contact book
    def add_contact(self, name: str, phone: str, email: str = None) -> None:
        """
        Adds a new contact to the contact book.
        
        Parameters:
        name: str -> The name of the contact.
        phone: str -> The phone number of the contact.
        email: str (optional) -> The email of the contact (defaults to None).
        """
        if name in self.contact:
            print("Contact already exists!")  # Expression: print message if contact exists
            return
        
        # Type: contact[name] -> dict
        # Expression: Set the contact's phone and email in the dictionary.
        self.contact[name] = {}  # Initialize an empty dictionary for the contact
        self.contact[name]["phone"] = phone  # Assign the phone to the contact
        self.contact[name]["email"] = email  # Assign the email (could be None)

    # Method to view all contacts in the contact book
    def view_contact(self) -> None:
        """
        Displays all the contacts stored in the contact book.
        """
        # Type: name -> str, info -> dict
        # Expression: Loop through the contacts and print each one.
        for name, info in self.contact.items():
            print(f"Name: {name}")  # Print the contact's name
            print(f"Phone: {info['phone']}")  # Print the contact's phone
            print(f"Email: {info['email']}")  # Print the contact's email
            print("_" * 50)  # Print a divider line for readability

    # Method to update an existing contact
    def update_contact(self, name: str, phone: str = None, email: str = None) -> None:
        """
        Updates the phone or email of an existing contact.
        
        Parameters:
        name: str -> The name of the contact to update.
        phone: str (optional) -> The new phone number (optional, defaults to None).
        email: str (optional) -> The new email address (optional, defaults to None).
        """
        if name in self.contact:
            # Expression: Update the phone if a new one is provided
            if phone:
                self.contact[name]["phone"] = phone
            # Expression: Update the email if a new one is provided
            if email:
                self.contact[name]["email"] = email
                
            print("Contact updated successfully!")  # Print success message
        else:
            print("Contact doesn't exist!")  # Print message if contact is not found

    # Method to delete a contact from the contact book
    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact from the contact book.
        
        Parameters:
        name: str -> The name of the contact to delete.
        """
        if name in self.contact:
            del self.contact[name]  # Expression: Remove the contact from the dictionary
            print("Contact deleted.")  # Print success message
        else:
            print("Contact not found.")  # Print message if contact is not found


if __name__ == "__main__":
    book = ContactBook()

while True:
    # Display the menu to the user
    print("\n\n Welcome to contact book application")
    print("1. add contact")
    print("2. edit contact")
    print("3. view contact")
    print("4. delete contact")
    print("5. Quit")

    # Get the user's choice
    user_choice = input("please choose a option: ")

    # Quit the application if the user chooses option 5
    if user_choice == "5":
        break

    # Add a new contact
    elif user_choice == "1":
        name = input("please enter contact name: ").strip()
        phone = input("please enter contact phone: ").strip()
        email = input("please enter contact email: ").strip()

        book.add_contact(name, phone, email)

    # Update an existing contact
    elif user_choice == "2":
        name = input("please enter contact name: ").strip()
        phone = input("please enter contact phone (leave blank to keep the same): ").strip()
        email = input("please enter contact email (leave blank to keep the same): ").strip()

        # Use phone/email only if the user provided new values
        book.update_contact(name, phone if phone else None, email if email else None)

    # View all contacts
    elif user_choice == "3":
        print("\n\n List of contacts: ")
        book.view_contact()

    # Delete a contact
    elif user_choice == "4":
        name = input("\nEnter contact name: ").strip()
        book.delete_contact(name)

    # Handle invalid options
    else:
        print("Invalid option. Please try again.")