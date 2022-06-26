# scraping www.amazon.com

import sys
#from importlib.resources import contents
import requests
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

try:
    r = requests.get(url)                     
                                #to hande any exception if occurs
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK :',url)
    print(error_type,'Line:',error_info.tb_lineno)

htmlcontent = r.text                                #to convert html into text
#print(htmlcontent)
soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup)                        #it brings html of given webpage
detail = soup.find_all('div', attrs={'class' : '_3pLy-c'})              #find div tag and class in html
# title = soup.title
# print(type(title.string[0]))
for i in detail:                        #to print content stored in detail 
    print(i.text)
    print("\n")                         #give space between 



