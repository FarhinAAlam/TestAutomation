from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#1 Open Browser

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
 #open website

driver.get("file:///C:/Users/DCL/Desktop/SQA/BITM12/Multiselect.html/MultiSelection.html")


option1 = driver.find_element(By.XPATH,"/html/body/select/option[1]")
option2 = driver.find_element(By.XPATH,"/html/body/select/option[2]")

option3 = driver.find_element(By.XPATH,"/html/body/select/option[3]")
option4 = driver.find_element(By.XPATH,"/html/body/select/option[4]")

ActionChains(driver).key_down(Keys.CONTROL).click(option1).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(option2).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(option3).key_up(Keys.CONTROL).perform()

driver.close()