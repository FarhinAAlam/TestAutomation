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

driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
driver.execute_script("window.scrollBy(0,500)","")
downld = driver.find_element(By.XPATH,"/html/body/main/section[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/a").click()
