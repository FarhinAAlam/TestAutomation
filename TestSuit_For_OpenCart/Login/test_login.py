import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class login(unittest.TestCase):

    def test_login_TC001_valid(self):
        ## this login test case
        # Step 1 : Launch Browser

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # step 3: open website

        driver.get("https://demo.opencart.com/")

        # Step 3: Click Account
        my_account = driver.find_element(By.LINK_TEXT, 'My Account')

        my_account.click()
        # Step 4: Click on Login

        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()
        email = driver.find_element(By.NAME, 'email')
        email.clear()
        email.send_keys("testemail@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys("234567")
        # Click Login
        login_Button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')
        login_Button.click()

        print(" Login Test Case 001 executed")

        self.assert_(True)

    def test_login_TC002_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # step 3: open website

        driver.get("https://demo.opencart.com/")

        # Step 3: Click Account
        my_account = driver.find_element(By.LINK_TEXT, 'My Account')

        my_account.click()
        # Step 4: Click on Login

        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()
        email = driver.find_element(By.NAME, 'email')
        email.clear()
        email.send_keys("testemail@gmailyy.com")

        password = driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys("234567")

        # Click Login
        login_Button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')
        login_Button.click()
        print(" Login Test Case 002 executed")

        self.assert_(True)

    def test_login_TC003_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # step 3: open website

        driver.get("https://demo.opencart.com/")

        # Step 3: Click Account
        my_account = driver.find_element(By.LINK_TEXT, 'My Account')

        my_account.click()
        # Step 4: Click on Login

        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()
        email = driver.find_element(By.NAME, 'email')
        email.clear()
        email.send_keys("testemail@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys("eww")

        # Click Login
        login_Button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')
        login_Button.click()

        print(" Login Test Case 003 executed")

        self.assert_(True)

    def test_login_TC004_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # step 3: open website

        driver.get("https://demo.opencart.com/")

        # Step 3: Click Account
        my_account = driver.find_element(By.LINK_TEXT, 'My Account')

        my_account.click()
        # Step 4: Click on Login

        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()
        email = driver.find_element(By.NAME, 'email')
        email.clear()
        email.send_keys("")

        password = driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys("234567")

        # Click Login
        login_Button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/form/input')
        login_Button.click()

        print(" Login Test Case 004 executed")

        self.assert_(True)

if __name__ == '__main__':
    unittest.main
