from dataclasses import dataclass


@dataclass
class AllBooksPageLocators:
    BOOKS: str = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
    PAGER: str = 'div.page_inner section ul.pager li.current'


@dataclass
class BookLocators:
    """
    Locators for an item in the HTML page.
    This allows us to easily see what our code will be looking at as well as change it quickly if
    we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
