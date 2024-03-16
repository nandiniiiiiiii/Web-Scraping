import sys
from playwright.sync_api import sync_playwright
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://in.indeed.com")

# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.ID,"text-input-what")),
#     EC.presence_of_element_located((By.ID,"text-input-where"))
# )

# input_ele = driver.find_element(By.ID,"text-input-what")
# input_ele2 = driver.find_element(By.ID,"text-input-where")
# input_ele.clear()
# driver.implicitly_wait(5)
# input_ele.send_keys(sys.argv[1])
# # input_ele.send_keys("IT")
# input_ele2.clear()
# input_ele2.send_keys(Keys.CONTROL + "a")
# input_ele2.send_keys(Keys.DELETE)
# input_ele2.send_keys("Mumbai" + Keys.ENTER)

print(sys.argv[1], "hello")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page1 = context.new_page()
    # page2 = context.new_page()
    page3 = context.new_page()

    page1.goto("https://www.flipkart.com/")
    box1 = page1.wait_for_selector('.Pke_EE')
    box1.type(sys.argv[1])
    page1.wait_for_selector('._2iLD__').click()
    
    # page2.goto("https://www.jiomart.com/")
    # box2 = page2.wait_for_selector('#twotabsearchtextbox')
    # box2.type(sys.argv[1])
    # page2.wait_for_selector('#nav-search-submit-button').click()
    # page2.wait_for_timeout(10000)

    page3.goto("https://www.snapdeal.com/")
    box3 = page3.wait_for_selector('#inputValEnter')
    box3.type(sys.argv[1])
    page3.wait_for_selector('.searchformButton').click()
    page3.wait_for_timeout(10000)

    browser.close()
