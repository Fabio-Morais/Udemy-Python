import re
from bs4 import BeautifulSoup
import logging

from locators.books_page_locators import QuotesPageLocators
from parsers.book import BookParser

logger = logging.getLogger('scraping.boos_page')

class BooksPages:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug('Finding all books in the page using ....')
        locator = QuotesPageLocators.BOOKS
        quote_tags = self.soup.select(locator) # for all books
        return [BookParser(e) for e in quote_tags]

    @property
    def page_numbers(self):
        logger.debug('Finding all number of catalogue pages available')
        locator = QuotesPageLocators.PAGER
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, self.soup.select_one(locator).string)
        logger.info('Found number of catalogue pages available')
        return int(matcher.group(1))