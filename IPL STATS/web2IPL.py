import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022#:~:text=TATA%20IPL%20Auction%20%2D%202022,IPL)%202022%20Auction%20in%20Bengaluru"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table', class_='ih-td-tab auction-tbl')
title = table.find_all('th')

header = []
for i in title:
    name = i.text
    header.append(name)

df = pd.DataFrame(columns=header)

rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all('td')[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all('td')[1:]
    row = [tr.text for tr in data]

    # row.insert(0, first_td)


    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row 


print(df)

df.to_csv('ipl2022.csv')
