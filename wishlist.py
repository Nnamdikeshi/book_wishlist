#Main program

import ui, datastore, fileio


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        sort_books()

    elif choice == '6':
        search_books()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    book_rating = ui.ask_for_book_rating()
    if datastore.set_read(book_id, book_rating):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    global counter

    new_book = ui.get_new_book_info()

    #print('in new_book')
    #print(new_book)

    counter = datastore.add_book(new_book, counter)
    ui.message('Book added: ' + str(new_book))


def sort_books():
    '''Sort books in Title or Author sequence based on user input'''

    mySort = ui.get_sort_order()
    datastore.sort_the_list(mySort)


def search_books():
    '''Search for a user specified book title and notify the user if found'''

    mySearch = ui.get_search_string()
    searchResult = datastore.get_books(search=mySearch)
    if searchResult != 'not found':
        print('This book was found: ', searchResult)
    else:
        print('The book was NOT found')


def quit():
    '''Perform shutdown tasks'''
    global counter

    #print ('in wishlist.py, about to shutdown, counter = ' + str(counter))

    fileio.shutdown(counter)
    ui.message('Bye!')


def main():
    global counter

    counter = fileio.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
