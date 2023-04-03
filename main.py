"""
This is a WebSite scrapping script
"""
from scrape import scrapes, extract
from store_SQL import store

# Get the url to scrape
URL = "http://programmer100.pythonanywhere.com/"

# Calling the module
if __name__ == "__main__":
    context = scrapes(URL)
    extraction = extract(context)
    store(extraction)

