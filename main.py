from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()

def getRandomTime():
    randTime = randint(3, 9)
    return randTime

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")
time.sleep(getRandomTime())



# //*[@id="loginForm"]/div[1]/div[1]/div/label/input
# element = driver.find_element_by_id("element_id")

username = os.environ.get('INSTAGRAM_USERNAME')
password = os.environ.get('INSTAGRAM_PASSWORD')

user_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
user_login.send_keys(username)

# //*[@id="loginForm"]/div[1]/div[2]/div/label/input
time.sleep(getRandomTime())

user_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
user_password.send_keys(password)

# //*[@id="loginForm"]/div[1]/div[3]/button
login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
login_btn.click()

driver.implicitly_wait(12)

time.sleep(19000)