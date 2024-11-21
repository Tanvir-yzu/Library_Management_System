import add_book
import view_book
import remove_book
import update_book

from icecream import ic
all_books = []

while True:
    # Display menu options
    ic("Library Management System")
    ic("0. Exit")
    ic("1. Add_Book")
    ic("2. View_Book")
    ic("3. Remove_Book")
    ic("4. Update_Book")

    # Get user input
    option = input("Enter option(0-4): ")

    
    if option == '0':
        break
    elif option == '1':
       add_book.add_book(all_books)
    elif option == '2':
       view_book.view_books(all_books) 
    elif option == '3':
       remove_book.remove_book(all_books)
    elif option == '4':
       update_book.update_book(all_books)
    else:
        ic("Invalid option")
