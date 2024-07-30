import json

def load_books():
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
    return books

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book(title, author, year):
    books = load_books()
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    save_books(books)

def get_books():
    books = load_books()
    return books

def search_books(title):
    books = load_books()
    return [book for book in books if book['title'].lower() == title.lower()]

def main_menu():
    while True:
        print("\n1. Add a book")
        print("2. View reading list")
        print("3. Search for a book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            year = input("Enter the year of publication: ")
            add_book(title, author, year)
            print(f"'{title}' by {author} ({year}) has been added to your reading list.")
        elif choice == '2':
            books = get_books()
            if books:
                print("\nYour reading list:")
                for book in books:
                    print(f"{book['title']} by {book['author']} ({book['year']})")
            else:
                print("\nYour reading list is empty.")
        elif choice == '3':
            title = input("Enter the title of the book to search: ")
            found_books = search_books(title)
            if found_books:
                print("\nBooks found:")
                for book in found_books:
                    print(f"{book['title']} by {book['author']} ({book['year']})")
            else:
                print("\nNo books found with that title.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
