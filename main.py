"""
This is a WebSite scrapping script
"""
from scrape import scrapes, extract
from store import store

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


if __name__ == "__main__":
    context = scrapes(URL)
    extraction = extract(context)
    store(extraction)

