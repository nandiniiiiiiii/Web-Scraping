import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://in.indeed.com")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,"text-input-what")),
    EC.presence_of_element_located((By.ID,"text-input-where"))
)

input_ele = driver.find_element(By.ID,"text-input-what")
input_ele2 = driver.find_element(By.ID,"text-input-where")
input_ele.clear()
driver.implicitly_wait(5)
input_ele.send_keys(sys.argv[1])   
# input_ele.send_keys("IT")   
input_ele2.clear()
input_ele2.send_keys(Keys.CONTROL + "a")  
input_ele2.send_keys(Keys.DELETE) 
input_ele2.send_keys("Mumbai" + Keys.ENTER)

# print(sys.argv[1],"hello");