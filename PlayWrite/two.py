from playwright.sync_api import sync_playwright
import time;

# def check_json(response):
#     print({"url":response.url, "body":response.json()})

def run(p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.on("response",lambda response: check_json(response))
    page.goto("https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    page.wait_for_timeout(1000)

    # to get a single element 
    # title_ele = page.wait_for_selector('.s1Q9rs')
    # title_text = title_ele.inner_text()
    # print(title_text)

    elements = page.query_selector_all('.s1Q9rs')
    for element in elements:
        # print(element.text())
        title = element.get_attribute('title')
        print(title)

    # infinite scroll
    # for x in range(1,3):
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    #     print("Scrolling",x)
    #     time.sleep(2)

    browser.close()

with sync_playwright() as p:
    run(p)