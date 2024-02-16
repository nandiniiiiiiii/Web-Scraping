from bs4 import BeautifulSoup
import requests
import pandas as pd

# functions
def get_title(new_soup):
    try:
        title = new_soup.find_all("span", attrs={"class": "B_NuCI"})
        title_val = title[0].text.strip()
    except:
        title_val = "__"
    return title_val


def get_price(new_soup):
    try:
        price = new_soup.find_all("div", attrs={"class": "_30jeq3 _16Jk6d"})
        price_val = price[0].text.strip()
    except:
        price_val = "__"
    return price_val


def get_rating(new_soup):
    try:
        rating = new_soup.find_all("div", attrs={"class": "_3LWZlK"})
        rating_val = rating[0].text.strip()
        # print(rating_val)
    except:
        rating_val = "__"
    return rating_val


def about_product(new_soup):
    # print("HIGHLIGHTS: ")
    arr = []
    try:
        reviews = new_soup.find_all("li", attrs={"class": "_21Ahn-"})
        for review in reviews:
            arr.append(review.text.strip())
            # print(review.text.strip())
    except:
        arr.append("__")
        # print("null")
    return arr;

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }
    URL = f"https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=0b85595a-82b5-4419-a000-9fad5c60f6ca"
    
    r = requests.get(URL, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a", attrs={"class": "_1fQZEK"})  # to get that individual element
    
    listOfLink = []
    for link in links:
        listOfLink.append(link.get("href"))
        d = {"title": [], "price": [], "rating": [], "highlights": []}
    for link in listOfLink:
        product_link = "https://flipkart.com" + link
        print(product_link)
        webpage = requests.get(product_link, headers)
        new_soup = BeautifulSoup(webpage.content, "html.parser")
        # print(new_soup)


        # function call
        d['title'].append(get_title(new_soup))
        # print(f"Title: {get_title(new_soup)}")
        d['price'].append(get_price(new_soup))
        # print(f"Price: {get_price(new_soup)}")
        d['rating'].append(get_rating(new_soup))
        # print(f"Rating: {get_rating(new_soup)}")
        d['highlights'].append(about_product(new_soup))
        # about_product(new_soup)
        print(d)
        df = pd.DataFrame.from_dict(d)
        df.to_csv("flipkart.csv",header=True,index=False)

# asyncio.run(main())
main()
