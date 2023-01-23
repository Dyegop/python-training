import re
from bs4 import BeautifulSoup
from locators import AllBooksPageLocators
from locators import BookLocators



class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item in it.
    In other words, this basically parses HTML page or content.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} {self.price}, {self.rating} stars>'

    @property
    def name(self):
        item_name = self.parent.select_one(selector=BookLocators.NAME_LOCATOR).attrs['title']
        print(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        item_url = self.parent.select_one(selector=BookLocators.LINK_LOCATOR).attrs['href']
        print(f'Found book page link, `{item_url}`.')
        return item_url

    @property
    def price(self):
        item_price = self.parent.select_one(selector=BookLocators.PRICE_LOCATOR).string
        matcher = re.search('£([0-9]+\\.[0-9]+)', item_price)
        price = float(matcher.group(1))
        print(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        star_rating_element = self.parent.select_one(selector=BookLocators.RATING_LOCATOR)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_class = next(rating_classes)
        rating = BookParser.RATINGS.get(rating_class)
        print(f'Found book rating, `{rating}`.')
        return rating




class AllBooksPage:
    """
    Class representation of all books in a page.
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        """ Returns the number of pages """
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        print(f'Found number of catalogue pages available: `{content}`')
        matcher = re.search('Page [0-9]+ of ([0-9]+)', content)
        pages = int(matcher.group(1))
        print(f'Extracted number of pages as integer: `{pages}`.')
        return pages
