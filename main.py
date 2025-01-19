from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")

title = driver.title
print(title)

time.sleep(190)
