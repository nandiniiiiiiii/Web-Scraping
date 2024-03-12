from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrapy

def rt(response):
    print(response.url)
    # playwrite
    pass

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://in.indeed.com")
# response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,"text-input-what")),
    EC.presence_of_element_located((By.ID,"text-input-where"))
)

input_ele = driver.find_element(By.ID,"text-input-what")
input_ele2 = driver.find_element(By.ID,"text-input-where")
# print(input_ele)
input_ele.clear()
driver.implicitly_wait(5)
input_ele.send_keys("IT")   
input_ele2.clear()
input_ele2.send_keys(Keys.CONTROL + "a")  
input_ele2.send_keys(Keys.DELETE) 
input_ele2.send_keys("Mumbai" + Keys.ENTER)   


jobs = []
# avalialbe_job = driver.find_elements(By.CLASS_NAME,"jcs-JobTitle css-jspxzf eu4oa1w0")
xpath = "//div[@class='job_seen_beacon']//a"
avalialbe_job = driver.find_elements(By.CLASS_NAME,"jcs-JobTitle")
print(avalialbe_job)
for job in avalialbe_job:
    href = job.get_attribute("href")
    # print(href)
    scrapy.Request(url=href,callback=rt)
    jobs.append(href)
# print(jobs)

time.sleep(10)        
driver.quit()