from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#1 Open Browser

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
 #open website

driver.get("https://demo.opencart.com/")
my_account = driver.find_element_by_link_text("My Account")

my_account.click()

login = driver.find_element_by_link_text("Login")
login.click()