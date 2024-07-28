import csv
import os

def initialize_csv():
    if not os.path.isfile('books.csv'):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Year"])

def add_book(title, author, year):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
    print(f'Book "{title}" by {author} added to the reading list.')

def retrieve_books():
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        books = list(reader)
    
    if not books:
        print("No books in the reading list.")
    else:
        print("Reading List:")
        for book in books:
            print(f'Title: {book[0]}, Author: {book[1]}, Year: {book[2]}')

def search_book(title):
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for book in reader:
            if book[0].lower() == title.lower():
                print(f'Found Book: Title: {book[0]}, Author: {book[1]}, Year: {book[2]}')
                return
    print(f'Book titled "{title}" not found.')

def menu():
    initialize_csv()
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Retrieve reading list")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            retrieve_books()
        elif choice == '3':
            title = input("Enter the title of the book to search for: ")
            search_book(title)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
