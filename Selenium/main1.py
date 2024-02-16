from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#will open google sleep for 10 sec then automaticaly quit(close the window)
# driver.get("https://google.com")
# time.sleep(10)        
# driver.quit()

driver.get("https://google.com")

#this will wait for 5 sec to find this ele 
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

input_ele = driver.find_element(By.CLASS_NAME,"gLFyf")
input_ele.clear()
input_ele.send_keys("tech with tim" + Keys.ENTER)      #to type hello in the selected input and then hit enter

WebDriverWait(driver,10).until(
    # EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Hello world"))
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech With Tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
link.click()

time.sleep(15)        
driver.quit()