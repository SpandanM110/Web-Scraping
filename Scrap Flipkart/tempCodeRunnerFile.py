

# for i in range(2,10):
#     url = "https://www.flipkart.com/search?q=mobiles+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+5g%7CMobiles&requestId=e3cdf399-983b-4a58-aa16-b67be94cc60b&as-searchtext=mobiles"

#     r = requests.get(url)
#     print(r)

#     soup = BeautifulSoup(r.text, "lxml")
# while True:
#     np = soup.find("a",class_="_1LKT03").get("href")
#     # print(np)

#     cnp = "https://www.flipkart.com" + np
#     print(cnp)

#     url= cnp
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, "lxml")

