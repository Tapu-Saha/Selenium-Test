from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://smallpdf.com/compress-pdf")
time.sleep(2)
print(driver.title)
driver.back()
driver.get("https://quillbot.com/")
time.sleep(2)
driver.forward()


