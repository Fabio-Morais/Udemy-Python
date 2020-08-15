import requests
import logging
from pages.books_page import BooksPages

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')# singleton pattern

logger.info('Loading books list....')

page_content = requests.get('http://books.toscrape.com/').content
page = BooksPages(page_content)

books = page.books
for page_num in range(1 , page.page_numbers):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = BooksPages(page_content)
    books.extend(page.books)