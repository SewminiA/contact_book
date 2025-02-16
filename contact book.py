#!/usr/bin/env python
# coding: utf-8

# In[1]:



contacts = []


def add():
    name = input("Enter name: ")
    number = input(f"Enter number for {name}: ")
    contacts.append((name, number)) 
    print(f"Contact for {name} added successfully!")


def view():
    if contacts:
        print("Contact list:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}")
    else:
        print("No contacts found.")


def search():
    search_name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if contact[0].lower() == search_name.lower():
            print(f"Name: {contact[0]}, Phone: {contact[1]}")
            found = True
            break
    if not found:
        print(f"No contact found with name {search_name}.")

def delete():
    delete_name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact[0].lower() != delete_name.lower()]
    print(f"Contact for {delete_name} deleted (if it existed).")


def update():
    update_name = input("Enter the name of the contact to update: ")
    for i, contact in enumerate(contacts):
        if contact[0].lower() == update_name.lower():
            new_number = input(f"Enter the new number for {contact[0]}: ")
            contacts[i] = (contact[0], new_number) 
            print(f"Contact for {update_name} updated successfully!")
            return
    print(f"No contact found with name {update_name}.")


def menu():
    while True:
     
        print("\n..Contact BOOK..\n")
        print("Contact book menu: ")
        print("1 - Add contact")
        print("2 - Search")
        print("3 - View all contacts")
        print("4 - Delete contact")
        print("5 - Update contact")
        print("6 - Exit")
        
        choice = int(input("What do you need (enter relevant number): "))
        
        if choice == 1:
            add()
        elif choice == 2:
            search()
        elif choice == 3:
            view()
        elif choice == 4:
            delete()
        elif choice == 5:
            update()
        elif choice == 6:
            print("Exiting Contact Book.")
            break
        else:
            print("Please enter a valid number.")


menu()


# In[ ]:




