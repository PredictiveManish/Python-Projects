import json
import os
import re

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                contacts = json.load(file)
                if not isinstance(contacts, dict):
                    return {}
                return contacts
            except json.JSONDecodeError:
                return {}
    else:
        with open(CONTACTS_FILE, "w") as file:
            json.dump({}, file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    
    if len(phone) != 10:
        print("Enter valid phone number.")
        return
    if not phone.isdigit():
        print("Phone number should contain only digits.")
        return
    
    email = input("Enter email ID: ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact: {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")
    
def delete_contact(contacts):
    name = input("Enter contact name you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found!")

def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found!")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved successfully! Exiting....")
            break
        else:
            print("Invalid choice, try again!!")

if __name__ == "__main__":
    main()
