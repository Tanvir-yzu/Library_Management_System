from save_book import save_book
from datetime import datetime

def add_book(all_books):
    try:
        # Input the book details
        title = input("Enter the title of the book: ").strip()
        author = input("Enter the author of the book: ").strip()

        # Validate publication year
        publication_year = int(input("Enter the publication year: "))
        current_year = datetime.now().year
        if publication_year <= 0 or publication_year > current_year:
            raise ValueError(f"Publication year  {current_year}.")

        # Validate ISBN and price
        ISBN = int(input("Enter the ISBN number of the book: "))
        price = int(input("Enter the price of the book: "))
        if price < 0:
            raise ValueError("Price cannot be negative.")

        # Validate quantity
        quantity = int(input("Enter the quantity of the book: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Check for duplicates based on ISBN
        for book in all_books:
            if book["ISBN"] == ISBN:
                print("A book with the same ISBN already exists.")
                return

        # Create a new book dictionary
        new_book = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "ISBN": ISBN,
            "price": price,
            "quantity": quantity
        }

        # Add the book to the list and save
        all_books.append(new_book)
        try:
            save_book(all_books)
            print("Book added and saved successfully!")
        except Exception as e:
            print(f"Failed to save book: {e}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
        
        # tanvir
