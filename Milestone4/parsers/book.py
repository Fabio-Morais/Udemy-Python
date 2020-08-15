from locators.books_locators import QuoteLocators
import re
import logging

logger = logging.getLogger('scraping.book')

class BookParser:

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
        return f'{self.name} \t<->\t {self.price} \t-> {self.rating} star'

    @property
    def name(self):
        locator = QuoteLocators.NAME
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = QuoteLocators.LINK
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = QuoteLocators.PRICE
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, self.parent.select_one(locator).string)
        return  float(matcher.group(1))

    @property
    def rating(self):
        locator = QuoteLocators.RATING
        aux = ""
        rating = aux.join([x for x in self.parent.select_one(locator).attrs['class'] if x != 'star-rating'])
        rating_number = BookParser.RATINGS.get(rating)
        return rating_number

