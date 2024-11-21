import csv

def save_book(all_books):
    # Specify the file name
    file_name = "book.csv"

    # Check if the list of books is empty
    if not all_books:
        print("No books to save.")
        return

    # Save books to a CSV file
    try:
        with open(file_name, "w", newline="") as fp:
            writer = csv.DictWriter(fp, fieldnames=["title", "author", "publication_year", "ISBN", "price", "quantity"])
            # Write headers
            writer.writeheader()
            # Write each book as a row
            writer.writerows(all_books)

        print(f"Books successfully saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred while saving books: {e}")
