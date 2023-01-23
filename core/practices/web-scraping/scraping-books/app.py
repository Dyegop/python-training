import requests
import time
from books import AllBooksPage



def get_books():
    _books = []

    print('Loading books list...')
    print('Requesting at http://books.toscrape.com')

    page_content = requests.get('http://books.toscrape.com').content
    page = AllBooksPage(page_content)
    start = time.time()

    for page_num in range(page.page_count):
        url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
        page_content = requests.get(url).content
        page = AllBooksPage(page_content)
        _books.extend(page.books)

    print(f'Total took {time.time() - start}')
    return _books


def print_best_books(books):
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)


def print_cheapest_books(books):
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


def get_next_book(books):
    books_generator = (x for x in books)
    print(next(books_generator))


def menu():
    user_choices = {
        'b': print_best_books,
        'c': print_cheapest_books,
        'n': get_next_book
    }

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            books = get_books()
            user_choices[user_input](books)
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)



if __name__ == "__main__":
    USER_CHOICE = '''Enter one of the following
    - 'b' to look at 5-star books
    - 'c' to look at the cheapest books
    - 'n' to just get the next available book on the page
    - 'q' to exit
    Enter your choice: '''


    menu()

