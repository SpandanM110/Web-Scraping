import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Price = []
Description = []
Reviews = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobiles+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+5g%7CMobiles&requestId=e3cdf399-983b-4a58-aa16-b67be94cc60b&as-searchtext=mobiles"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    boxes = soup.find_all("div", class_="_1AtVbE")
    names = soup.find_all("div", class_="_4rR01T")
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    descriptions = soup.find_all("ul", class_="_1xgFaf")
    reviews = soup.find_all("div", class_="_3LWZlK")

    for name in names:
        Product_Name.append(name.text)

    for price in prices:
        Price.append(price.text)

    for desc in descriptions:
        Description.append(desc.text)

    for review in reviews:
        Reviews.append(review.text)

df = pd.DataFrame({"Product Name": Product_Name[:len(Price)], "Price": Price, "Description": Description[:len(Price)], "Reviews": Reviews[:len(Price)]})
print(df)

df.to_csv("flipkart.csv")
