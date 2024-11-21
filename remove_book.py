def remove_book(all_books):
    if not all_books:
        print("No books available to remove.")
        return

    try:
        ISBN_to_remove = int(input("Enter the ISBN of the book to remove: "))
        
        # Find the book by ISBN
        for book in all_books:
            if book["ISBN"] == ISBN_to_remove:
                all_books.remove(book)
                print("Book removed successfully!")
                return
        
        print("Book with the specified ISBN not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")
