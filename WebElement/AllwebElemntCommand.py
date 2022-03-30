from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

    ## this login test case
#Step 1 : Launch Browser

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
 #step 3: open website

driver.get("https://demo.opencart.com/")

#Step 3: Click Account
my_account = driver.find_element(By.LINK_TEXT, 'My Account')

my_account.click()
#Step 4: Click on Login

login = driver.find_element(By.LINK_TEXT, 'Login')
login.click()

#step 5 :  Type/Enter text
email = driver.find_element(By.ID, 'input-email')
email.clear()
email.send_keys("testemail@gmail.com")

#step 6  Type password

password = driver.find_element(By.ID,'input-password')
password.click()
password.send_keys("234567")

#step 7 click login button
login = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
login.click()
