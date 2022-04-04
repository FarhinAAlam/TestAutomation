from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

#NormalAlart

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

normalAlart = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button')
normalAlart.click()
driver.switch_to.alert.accept()   #ok

#confirmAlart
confirm_alart = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button')

confirm_alart.click()
driver.switch_to.alert.dismiss()

#prompt

promt = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button')
promt.click()
driver.switch_to.alert.send_keys("Testing ")

#print korte chaile alarm text

title_promt = driver.switch_to.alert.text
print( ' Promt alart title is : '  + title_promt)

driver.switch_to.alert.accept()







