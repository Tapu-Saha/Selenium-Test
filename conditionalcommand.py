from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.aiub.edu/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/ul/li[1]/a/span").click()
time.sleep(2)
user_ele = driver.find_element(By.NAME, "UserName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element(By.NAME, "Password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())


