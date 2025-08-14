contacts = []

# Add new contact
def add_contact():
    store_name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        "store_name": store_name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    print("Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['store_name']} - {contact['phone']}")
    print()

# Search contact
def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['store_name'].lower() or keyword in contact['phone']:
            print("Contact Found:")
            print_contact(contact)
            found = True
    if not found:
        print("No contact found.\n")

# Update contact
def update_contact():
    phone = input("Enter the phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Current details:")
            print_contact(contact)
            contact['store_name'] = input("Enter new Store Name: ")
            contact['phone'] = input("Enter new Phone Number: ")
            contact['email'] = input("Enter new Email: ")
            contact['address'] = input("Enter new Address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

# Delete contact
def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['phone'] == phone:
            print(f"Deleting contact: {contact['store_name']} - {contact['phone']}")
            del contacts[i]
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

# Helper function to print contact
def print_contact(contact):
    print(f"Store Name : {contact['store_name']}")
    print(f"Phone      : {contact['phone']}")
    print(f"Email      : {contact['email']}")
    print(f"Address    : {contact['address']}\n")

# Menu
def menu():
    while True:
        print("==== Contact Management System ====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
