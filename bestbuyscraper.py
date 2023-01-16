import requests, ezgmail
from bs4 import BeautifulSoup

url = "https://www.bestbuy.ca/en-ca/product/apple-airpods-pro-2nd-generation-in-ear-noise-cancelling-truly-wireless-headphones-white/16486693" #product URL of choice

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

productTitle = soup.find(class_='productName_2KoPa').get_text() # this class works for all BB products
availabilityMessage = soup.find(class_='availabilityMessage_3ZSBM container_1DAvI').get_text() # this class works for all BB products

if availabilityMessage == "Available to ship":
    ezgmail.send('youremailhere', productTitle, "Hi! Your product is available to be shipped on Best Buy!") #sends email to desired email with an appropriate message
    print("Message has been sent!")