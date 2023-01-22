from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.alibaba.com/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[4]/div[1]/div[1]/div[2]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/form/div[6]/div[1]/a").click()


