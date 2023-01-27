from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
ts = driver.find_element(By.NAME,'userName')
print(ts.is_displayed())
print(ts.is_enabled())
ts.send_keys('Tapu')
time.sleep(2)
driver.find_element(By.NAME,'password').send_keys('1234')
time.sleep(2)
driver.find_element(By.NAME,'submit').click()
time.sleep(2)






