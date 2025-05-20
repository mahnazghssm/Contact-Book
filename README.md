# 📒 Contact Book Application

A simple, console-based contact book application written in Python. This tool allows you to add, update, view, and delete contact details such as names, phone numbers, and optional email addresses — all through an interactive menu.



## ✨ Features

	•	✅ Add new contacts with name, phone number, and optional email.
	•	📋 View all saved contacts in a clean format.
	•	✏️ Update phone numbers or emails for existing contacts.
	•	🗑️ Delete contacts by name.
	•	🧠 Input validation with error handling.
	•	📦 Uses defaultdict for dynamic dictionary handling.

## 🛠️ How to Use

1. Clone the Repository:
```
git clone https://github.com/mahnazghassemi/contact-book.git
cd contact-book
```
2.	Run the Application:

	To run the contact book, simply execute the following command:
```
	python contact_book.py
```
## 📜 Menu Options
When you run the program, you will see the following options:

📒 Welcome to the Contact Book Application!
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete Contact
5. Quit

	•	1. Add Contact – Input name, phone, and optional email. Prevents duplicates.
	•	2. Edit Contact – Update phone/email. Leave blank to keep unchanged.
	•	3. View Contact – Displays a list of all saved contacts.
	•	4. Delete Contact – Removes a contact by name.
	•	5. Quit – Exits the application.


## 📂 Code Structure
•	ContactBook class manages all contact records using a defaultdict.

•	Each contact is stored as a nested dictionary:

```
{
  "Alice": {
      "phone": "12345",
      "email": "alice@example.com"
  }
}
```
## 🧠 Key Methods

| Method | Description |
|--------|-------------|
| add_contact(name, phone, email=None) | Adds a new contact with the given name, phone, and optional email. Prevents duplicates. |
| view_contact() | Displays all saved contacts in a clean and formatted way. |
| update_contact(name, phone=None, email=None) | Updates the phone number and/or email of an existing contact. |
| delete_contact(name) | Deletes the contact with the specified name if it exists. |


## 📌 Example Usage

book = ContactBook()

book.add_contact("Alice", "12345", "alice@example.com")
book.view_contact()
book.update_contact("Alice", phone="54321")
book.delete_contact("Alice")

## 🐍 Requirements

•	Python 3.7 or higher

•	No external dependencies required (defaultdict is from the standard library)

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, or distribute it for educational or personal purposes.
