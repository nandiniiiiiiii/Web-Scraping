import scrapy
import pandas as pd
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://NandiniNegi:nandini123@cluster0.tuvn301.mongodb.net")
db = client.webscraping
def insertToDb(page,title,rating,price,instock):
    collection = db[page]
    doc = {
        "title" : title,
        "rating" : rating,
        "price" : price,
        "instock" : instock,
        "date" : datetime.datetime.utcnow(),
    }
    post_id = collection.insert_one(doc).inserted_id
    return post_id


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        print(page)
        d = {"title":[],"rating":[],"price":[],"availability":[]}
        cards = response.css(".product_pod")
        for card in cards:
            # title = card.css("h3>a::text").get()
            title = card.css("h3>a").attrib["title"]
            d['title'].append(title)
            # print(title)
            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
            d['rating'].append(rating)
            # print(rating)
            price = card.css(".price_color::text").get()
            d["price"].append(price)
            # print(price)
            availability = card.css(".availability")
            instock = False
            if len(availability.css(".icon-ok")) > 0:
                instock = True
                d["availability"].append("instock")
                # print("instock")
            else:
                d["availability"].append("not in instock")
                # print("not in stock")
            df = pd.DataFrame.from_dict(d)
            df.to_csv("flipkart.csv",header=True,index=False)
            # df.to_excel('flipkart.xlsx',header=True,index=False)     
            # insertToDb(page,title,rating,price,instock)