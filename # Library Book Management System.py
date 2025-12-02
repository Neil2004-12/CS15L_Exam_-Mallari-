# Library Book Management System
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True  # Default availability of the book

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"\nYou have successfully borrowed '{self.title}'.")
        else:
            print(f"\nSorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\nThank you for returning '{self.title}'.")
        else:
            print(f"\n'{self.title}' is not borrowed.")

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print("\n| Book Information |")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.year}")
        print(f"Status: {status}")


# Main program
print("| Library Book Management System |")

# Book details to get
title = input("Enter book title: ")
author = input("Enter author name: ")
year = input("Enter publication year: ")

# Create Book object
book = Book(title, author, year)

# Menu List
while True:
    print("\nWhat would you like to do?")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Display Book Information")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        book.borrow_book()
    elif choice == "2":
        book.return_book()
    elif choice == "3":
        book.display_info()
    elif choice == "4":
        print("\nExiting program... Thank You!")
        break
    else:
        print("\nInvalid choice. Please select 1–4.")
