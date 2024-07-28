import csv
import os

def initialize_csv():
    if not os.path.isfile('books.csv'):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Year", "Read"])

def add_book(title, author, year, read):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year, read])
    print(f'Book "{title}" by {author} added to the reading list.')

def retrieve_books():
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        books = list(reader)
    
    if not books:
        print("No books in the reading list.")
    else:
        print("Reading List:")
        for book in books:
            read_status = 'Read' if book[3] == 'yes' else 'Not read'
            print(f'Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Status: {read_status}')

def search_book(title):
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for book in reader:
            if book[0].lower() == title.lower():
                read_status = 'Read' if book[3] == 'yes' else 'Not read'
                print(f'Found Book: Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Status: {read_status}')
                return
    print(f'Book titled "{title}" not found.')

def mark_book_as_read(title):
    books = []
    found = False
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for book in reader:
            if book[0].lower() == title.lower() and not found:
                book[3] = 'yes'
                found = True
            books.append(book)
    
    if found:
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(books)
        print(f'Book titled "{title}" marked as read.')
    else:
        print(f'Book titled "{title}" not found.')

def delete_book(title):
    books = []
    found = False
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for book in reader:
            if book[0].lower() == title.lower() and not found:
                found = True
                continue
            books.append(book)
    
    if found:
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(books)
        print(f'Book titled "{title}" deleted from the reading list.')
    else:
        print(f'Book titled "{title}" not found.')

def menu():
    initialize_csv()
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Retrieve reading list")
        print("3. Search for a book")
        print("4. Mark a book as read")
        print("5. Delete a book")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            year = input("Enter year of publication: ")
            read = input("Has the book been read? (yes/no): ")
            add_book(title, author, year, read)
        elif choice == '2':
            retrieve_books()
        elif choice == '3':
            title = input("Enter the title of the book to search for: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter the title of the book to mark as read: ")
            mark_book_as_read(title)
        elif choice == '5':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
