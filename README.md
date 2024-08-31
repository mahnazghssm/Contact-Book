# Contact Book Application
A simple console-based application written in Python for managing contact information, such as names, phone numbers, and email addresses. The application allows you to add, update, view, and delete contacts interactively.

## Features
•	Add a new contact with a name, phone number, and optional email.
•	View a list of all saved contacts.
•	Update existing contact details, including phone numbers and emails.
•	Delete contacts by name.
•	Interactive console-based user interface.

## How to Use

1. Clone the Repository:
```
git clone https://github.com/yourusername/contact-book.git
cd contact-book
```
2.	Run the Application:
To run the contact book, simply execute the following command:
```
python contact_book.py
```
3.	Menu Options:
When you run the program, you will see the following options:

Welcome to contact book application

1. Add contact
2. Edit contact
3. View contacts
4. Delete contact
5. Quit

	•	Option 1: Add a contact

	•	Input the contact’s name, phone number, and an optional email.

	•	If the contact already exists, the system will notify you.

	•	Option 2: Edit a contact

	•	Update the phone number and/or email for an existing contact.

	•	Leave the field blank if you don’t want to update it.

	•	Option 3: View contacts

	•	Display a list of all the contacts saved in the system.

	•	Option 4: Delete a contact

	•	Delete a contact from the system by entering the contact’s name.

	•	Option 5: Quit

	•	Exit the application.



## Code Overview

The application is built with Python and consists of two main parts:
```
1.	ContactBook Class:
	•	Manages all contacts using a dictionary.
	•	Functions for adding, updating, viewing, and deleting contacts.

2.	Interactive Menu:
	•	Displays a menu to the user and handles input to trigger the correct actions.
```
ContactBook Class

	•	add_contact(name, phone, email=None): Adds a new contact to the contact book.
	•	view_contact(): Displays all contacts in the book.
	•	update_contact(name, phone=None, email=None): Updates an existing contact’s phone or email.
	•	delete_contact(name): Deletes a contact by name.
    


## Example Code

### Example of adding a contact:
book = ContactBook()
book.add_contact("Alice", "12345", "alice@example.com")

Example of viewing all contacts:
book.view_contact()

### Example of updating a contact:
book.update_contact("Alice", phone="54321")

### Example of deleting a contact:
book.delete_contact("Alice")

## Requirements
•	Python 3.x

No external libraries are required.

## License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

This README.md explains how to use the contact book application, how to run it, and gives an overview of the main features and code structure. You can modify it further to suit any additional features you may want to include.