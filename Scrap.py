# scraping www.amazon.com

from importlib.resources import contents
from turtle import title
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup)
title = soup.title
print(type(title.string))