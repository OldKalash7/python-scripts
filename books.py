# Script for webscraping the read list of books of Goodreads.

from bs4 import BeautifulSoup
import requests

def main():
    booklist = "https://www.goodreads.com/review/list/46559081"

    web = requests.get(booklist)

    soup = BeautifulSoup(web, 'html.parser')

    print(soup.prettify())



main()
