import csv

# 1. Contact class with validation
class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain digits only")
        self.name = name
        self.phone_number = phone_number

# 2. PhoneBook class with file handling
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        try:
            contact = Contact(name, phone)
            self.contacts.append(contact)
            print("Contact added successfully.")
        except ValueError:
            print("Invalid phone number format. Try again.")

    def save_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone_number])
            print("Contacts saved to file.")
        except Exception as e:
            print("Error saving to file:", e)

    def load_from_csv(self, filename):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        name, phone = row
                        try:
                            contact = Contact(name, phone)
                            self.contacts.append(contact)
                        except ValueError:
                            print(f"Skipped invalid contact: {name} - {phone}")
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("No file found. Starting with an empty phone book.")

# 3. Main menu (user interface)
def main():
    phonebook = PhoneBook()
    phonebook.load_from_csv("contacts.csv")

    while True:
        print("\nContact Manager Menu")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Save and Exit")

        try:
            choice = int(input("Choose an option (1-3): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phonebook.add_contact(name, phone)

        elif choice == 2:
            if not phonebook.contacts:
                print("No contacts found.")
            else:
                print("\nContact List:")
                for i, c in enumerate(phonebook.contacts, 1):
                    print(f"{i}. {c.name} - {c.phone_number}")

        elif choice == 3:
            phonebook.save_to_csv("contacts.csv")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    main()