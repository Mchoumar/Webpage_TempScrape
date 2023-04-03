"""
This script get the url data and extract the temperature
"""

import requests
from selectorlib import Extractor

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrapes(url):
    """Scraps the data from the website"""
    print("Extracting...")
    request = requests.get(url, headers=HEADERS)
    source = request.text

    return source


def extract(source_url):
    """Extracting object from the website"""
    extractor = Extractor.from_yaml_file('temperature.yaml')
    value = extractor.extract(source_url)['temps']

    print("Extracting Done!")

    return value


if __name__ == "__main__":
    sources = scrapes("http://programmer100.pythonanywhere.com/")
    print(extract(sources))
