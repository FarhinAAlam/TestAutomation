from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions
options.headless = True

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://translate.google.com/")

print(' Title is : ' + driver.title)