from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.google.com/")
driver.get_screenshot_as_file("C:\Users\DCL\Desktop\SQA\BITM12\TestAutomation\SSFiles\google.jpg")
