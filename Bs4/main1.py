from bs4 import BeautifulSoup
import requests
import pandas as pd

# header is required: 1- (User-Agent)request look more like it's coming from a real user. 
#                     2- (Cookies)If a website requires authentication or session management, you may need to include cookies in the request headers to access certain pages or data.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}
URL = f"https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=0b85595a-82b5-4419-a000-9fad5c60f6ca"

r = requests.get(URL, headers)
#we can also write requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")

link = soup.find_all('a',attrs={'class':'_1fQZEK'})        #seleting all the a tags
# print(link)
# print(link[0].get('href'))
href_link = link[0].get('href')
product_link = "https://flipkart.com"+href_link             #getting links of all the tags
# print(product_link)

product_webpage = requests.get(product_link,headers)
product_soup = BeautifulSoup(product_webpage.content, "html.parser")
# print(product_soup)

title = product_soup.find_all('span',attrs={'class' : 'B_NuCI'})
print(title[0].text.strip())
price = product_soup.find_all('')