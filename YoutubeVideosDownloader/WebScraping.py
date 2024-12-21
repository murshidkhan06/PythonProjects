
## A simple web scraping example to get the title of a webpage.


import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

url = "https://www.youtube.com"
print(f"Page title: {get_page_title(url)}")