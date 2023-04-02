"""
This script get the url data and extract the temperature
"""

import requests
from selectorlib import Extractor


def scrapes(url):
    """Scraps the data from the website"""
    print("Extracting...")
    request = requests.get(url)
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
