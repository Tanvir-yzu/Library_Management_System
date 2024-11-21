def view_books(all_books):
    # Check if the library has books
    if not all_books:
        print("No books are currently available in the library.")
        return

    # Display the books in a readable format
    print("\nList of Books in the Library:")
    print("-" * 50)
    for index, book in enumerate(all_books, start=1):
        print(f"Book {index}:")
        print(f"  Title           : {book['title']}")
        print(f"  Author          : {book['author']}")
        print(f"  Publication Year: {book['publication_year']}")
        print(f"  ISBN            : {book['ISBN']}")
        print(f"  Price           : ${book['price']}")
        print(f"  Quantity        : {book['quantity']}")
        print("-" * 50)
