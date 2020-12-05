import requests
import bs4 
import time
from bs4 import BeautifulSoup



r = requests.get('https://finance.yahoo.com/quote/NVDA?=NVDA')
soup = bs4.BeautifulSoup(r.text, "lxml")

soup.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

def nvidia_price():
    r = requests.get('https://finance.yahoo.com/quote/NVDA?=NVDA')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    price = soup.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

while True:
    print("the current price of the Nvidia Stock is: "+ str(nvidia_price()))
    time.sleep(5)
