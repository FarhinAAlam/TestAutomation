from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#1 Open Browser

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
 #open website

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID,' dropdown')

dropdownOptions =  Select(dropdown)

options =  Select(dropdown)
options.select_by_visible_text('Options 2')
