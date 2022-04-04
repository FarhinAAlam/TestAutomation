from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver =  webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown = driver.find_element(By.ID,"dropdown")

options = Select(dropdown)
#options.select_by_index(1)
#or ucan use
options.select_by_value("1")
#driver.close()