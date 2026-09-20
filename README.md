# Contact Book

A simple console-based Contact Book application written in Python.

The application allows users to add, view, edit, and delete contacts. Each contact includes a name, phone number, email, and address.

## CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

In this project:

- **Create**: Add a new contact
- **Read**: View saved contacts
- **Update**: Edit contact information
- **Delete**: Delete a contact

## Project Structure

```text
.
├── README.md
├── .gitignore
└── src
    └── main.py
```

- `README.md`: Project documentation
- `.gitignore`: Files and folders ignored by Git
- `src/main.py`: Contains the `ContactBook` class and the main application

## ContactBook Class

The `ContactBook` class manages contacts using a Python dictionary.

Each contact contains a phone number, email, and address, and is stored using the contact's name as the key.

```python
{
    "Alice": {
        "phone": "12345",
        "email": "alice@example.com",
        "address": "New York"
    }
}
```

The class includes four main methods:

| Method             | Description                 |
| ------------------ | --------------------------- |
| `add_contact()`    | Adds a new contact          |
| `view_contacts()`  | Displays all contacts       |
| `edit_contact()`   | Updates contact information |
| `delete_contact()` | Deletes a contact           |

## User Interface

The application uses a simple console-based menu:

```text
--- Contact Book Application ---

1. Add contact
2. Edit contact
3. View contacts
4. Delete contact
5. Quit
```

When adding a contact, the user enters:

```text
Enter Contact name:
Enter Contact phone:
Enter Contact email:
Enter Contact address:
```

When editing a contact, the user can leave a field blank to keep the existing information.

## Requirements

- Python 3.x

No external packages are required.

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/mahnazghssm/Contact-Book.git
cd Contact-Book
```

Run the application:

```bash
python src/main.py
```

## What I Practiced

- Python classes and objects
- Dictionaries
- CRUD operations
- Functions and methods
- User input
- Basic project structure

## License

This project is licensed under the MIT License.
