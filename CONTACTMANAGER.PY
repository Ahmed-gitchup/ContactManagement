class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print("---------------------")


contact_manager = ContactManager()

while True:
    print("Contact Manager Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        email = input("Enter contact email: ")
        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter contact name to remove: ")
        contact_manager.remove_contact(name)

    elif choice == "3":
        name = input("Enter contact name to search: ")
        searched_contact = contact_manager.search_contact(name)
        if searched_contact:
            print("Contact found:")
            print(searched_contact)
        else:
            print("Contact not found.")

    elif choice == "4":
        contact_manager.display_contacts()

    elif choice == "5":
        print("Exiting Contact Manager...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")