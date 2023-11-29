from selenium import webdriver
from selenium.webdriver.common.by import By
import login_details
import time
username = login_details.username
password = login_details.password

driver = webdriver.Edge()
driver.get("http://172.16.40.5:8090/")
#driver.maximize_window()
#driver.get('https://bing.com')

#element = driver.find_element(By.ID, 'username')
#element.send_keys('balkrishna')
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID,"loginbutton").click()
time.sleep(5)
#driver.quit()