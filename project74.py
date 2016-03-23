#Python3
#The Tech Academy Python 74

from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the HTML from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
