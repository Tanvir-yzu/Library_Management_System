def update_book(all_books):
    if not all_books:
        print("No books available to update.")
        return

    try:
        ISBN_to_update = int(input("Enter the ISBN of the book to update: "))
        
        # Find the book by ISBN
        for book in all_books:
            if book["ISBN"] == ISBN_to_update:
                print(f"Updating details for book: {book['title']} by {book['author']}")

                
                book["title"] = input(f"Enter new title (current: {book['title']}): ") or book["title"]
                book["author"] = input(f"Enter new author (current: {book['author']}): ") or book["author"]
                try:
                    book["publication_year"] = int(input(f"Enter new publication year (current: {book['publication_year']}): ") or book["publication_year"])
                except ValueError:
                    print("Invalid year. Keeping the current value.")
                
                try:
                    book["price"] = int(input(f"Enter new price (current: {book['price']}): ") or book["price"])
                except ValueError:
                    print("Invalid price. Keeping the current value.")
                
                try:
                    book["quantity"] = int(input(f"Enter new quantity (current: {book['quantity']}): ") or book["quantity"])
                except ValueError:
                    print("Invalid quantity. Keeping the current value.")

                print("Book details updated successfully!")
                return
        
        print("Book with the specified ISBN not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")
