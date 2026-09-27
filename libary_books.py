from datetime import date





def display_books():
    print('Here are the available books we have:')
    print('')

    file = open('libary_catalog.txt', 'r')

    books = []

    for line in file:
        data = line.split(',')
        books.append(data[1].strip())

    file.close()

    for book in books:
        print(book)

    return books


def check_book_availability():

    book = input('Enter the book you want to check: ')

    file = open('libary_catalog.txt', 'r')

    lines = file.readlines()

    file.close()

    for i in range(len(lines)):
        data = lines[i].split(',')

        if book == data[1].strip():

            copies = int(data[5].strip())

            if copies > 0:

                print('The book,', book, 'has', copies, 'copies available.')

                ans = input('Would you like to borrow it? (yes, no): ').lower()

                if ans == 'yes':
                    borrow_book(book)
                else:
                    print('You did not borrow the book.')

            else:
                print('The book is not available.')

            return

    print('The book was not found.')


def borrow_book(book):

    name = input('Enter the name the book will be borrowed under: ')
    how_many = int(input('Enter how many copies you want to borrow: '))

    file = open('libary_catalog.txt', 'r')

    lines = file.readlines()

    file.close()

    for i in range(len(lines)):

        data = lines[i].split(',')

        if book == data[1].strip():

            copies = int(data[5].strip())

            if how_many <= copies:

                copies = copies - how_many

                data[5] = ' ' + str(copies) + '\n'

                lines[i] = ','.join(data)

                print('You borrowed:', book)
                print('Copies left:', copies)

                book_borrow_info = name + ', ' + book + ', ' + str(how_many) + '\n'

                file = open('borrowed_books.txt', 'a')

                file.write(book_borrow_info)

                file.close()

                book_borrow_history = name + ', ' + 'borrowed' + ', ' + book + ', ' + str(how_many) + ', ' + str(date.today()) + '\n'

                file = open('borrowed_history.txt', 'a')

                file.write(book_borrow_history)

                file.close()


            else:
                print('There are not enough copies available.')

            break

    file = open('libary_catalog.txt', 'w')

    file.writelines(lines)

    file.close()


def return_book():

    name = input('Enter your name: ')

    file = open('borrowed_books.txt', 'r')

    lines = file.readlines()

    file.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].split(',')

        if name == data[0].strip():

            found = True

            book = data[1].strip()
            books_taken = int(data[2].strip())

            print('You have borrowed', books_taken, 'copies of', book)

            return_books = input('Would you like to return it? (yes, no): ').lower()

            if return_books == 'yes':

                file = open('libary_catalog.txt', 'r')

                catalog_lines = file.readlines()

                file.close()

                for j in range(len(catalog_lines)):

                    catalog_data = catalog_lines[j].split(',')

                    if book == catalog_data[1].strip():

                        copies = int(catalog_data[5].strip())

                        total_copies = int(catalog_data[4].strip())

                        copies = copies + books_taken

                        if copies > total_copies:
                            copies = total_copies

                        catalog_data[5] = ' ' + str(copies) + '\n'

                        catalog_lines[j] = ','.join(catalog_data)

                        break

                file = open('libary_catalog.txt', 'w')

                file.writelines(catalog_lines)

                file.close()

                print('You returned:', book)

                lines.pop(i)

                file = open('borrowed_books.txt', 'w')

                file.writelines(lines)

                file.close()


                return_book_history = name + ', ' + 'returned' + ', ' + book + ', ' + str(books_taken) + ', ' + str(date.today()) + '\n'

                file = open('borrowed_history.txt', 'a')

                file.write(return_book_history)

                file.close()

            break

    if found == False:
        print('You have not borrowed any books.')


def add_book():

    while True:
        book_id = input('Enter Book ID: ')

        file = open('libary_catalog.txt', 'r')

        valid = True

        for line in file:
            data = line.split(',')

            if book_id == data[0].strip():
                valid = False
                break

        file.close()

        if valid:
            break

        print('That Book ID already exists. Please enter a different ID.')

    title = input('Enter title: ')
    author = input('Enter author: ')
    genre = input('Enter genre: ')
    copies = int(input('Enter number of copies: '))

    new_book = book_id + ', ' + title + ', ' + author + ', ' + genre + ', ' + str(copies) + ', ' + str(copies) + '\n'

    file = open('libary_catalog.txt', 'a')

    file.write(new_book)

    file.close()

    print(new_book)
    print('was added')


def remove_book():


    book = input('Enter the book ID of the book you want to remove (001 or 002 ect): ')

    file = open('libary_catalog.txt', 'r')

    lines = file.readlines()

    file.close()

    for i in range(len(lines)):
        data = lines[i].split(',')

        if book == data[0]:
            lines.pop(i)
            file = open('libary_catalog.txt', 'w')
            file.writelines(lines)
            file.close()

            print('The book was removed.')
            return
        
        
    print('Book not found')


def search_books():

    search_by = input('what would you like to search by? (Title, Author, Genre): ').lower()

    if search_by == 'title':
        num = 1
    elif search_by == 'author':
        num = 2
    elif search_by == 'genre':
        num = 3
    else:
        print('Invalid choice.')
        return

    search_term = input('Enter the ' + search_by + ' you are looking for: ')

    file = open('libary_catalog.txt', 'r')

    lines = file.readlines()

    file.close()

    found = False

    for i in range(len(lines)):
        data = lines[i].split(',')

        if data[num].strip().lower() == search_term.lower():
            found = True
            print(data[1].strip(), ',', data[2].strip(), ',', data[3].strip(), ',', data[4].strip(), ',', data[5].strip())

    if not found:
        print('No matching books found.')




#the program

while True:
    print('')
    print('--- Library Menu ---')
    print('1. Display all books')
    print('2. Check / borrow a book')
    print('3. Return a book')
    print('4. Add a book')
    print('5. Remove a book')
    print('6. Search for books')
    print('7. Quit')

    choice = input('Enter your choice (1-7): ')

    if choice == '1':
        display_books()
    elif choice == '2':
        check_book_availability()
    elif choice == '3':
        return_book()
    elif choice == '4':
        add_book()
    elif choice == '5':
        remove_book()
    elif choice == '6':
        search_books()
    elif choice == '7':
        print('Goodbye!')
        break
    else:
        print('Invalid choice, please enter a number from 1 to 7.')