def add_book(reading_list):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    book = {"title": title, "author": author, "year": year}
    reading_list.append(book)
    print(f"'{title}' by {author} ({year}) has been added to your reading list.")

def display_books(reading_list):
    if not reading_list:
        print("Your reading list is empty.")
    else:
        for idx, book in enumerate(reading_list, start=1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

def show_menu():
    print("\nMenu:")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Quit")
def main():
    reading_list = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(reading_list)
        elif choice == '2':
            display_books(reading_list)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
