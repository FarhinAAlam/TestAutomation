
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

file = driver.find_element(By.NAME,'upfile')

#file upload pattern holo endkeys vitor path url\filename

file.send_keys('C:\Users\DCL\Desktop\SQA\BITM12\TestAutomation\HELLO!Farhina')
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/form/input[3]').click()
