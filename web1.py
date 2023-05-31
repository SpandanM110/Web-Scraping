import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup)

#in order to find the details of the page from a particular tag
boxes = soup.find_all("div", class_="col-sm-4 col-lg-4 col-md-4")
# print(boxes)

# in order to find the length of the page
# print(len(boxes))


#in order to print names from the page
names = soup.find_all("a", class_="title")
# print(names)

#in order to print the text from the page using for loop

for i in names:
    print(i.text)

#in order to print the price from the page
prices = soup.find_all("h4",class_="pull-right price")
print(prices)
