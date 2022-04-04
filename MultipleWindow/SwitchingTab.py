from  selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/windows")

parent_GUID = driver.current_window_handle   #single tab jonno eta  r micro window jonno driver.window_handles
print(parent_GUID)   #Run korale  ekekbar ekek id show/print korbe cz id ghula multiple window handle kore

driver.find_element(By.LINK_TEXT,'Click Here').click()
ALL_GUID = driver.window_handles
print(ALL_GUID)

# koroghula window ache jante chaile eta use korbe
print(len(ALL_GUID))

#switching new window to another(child) window
for child_window in ALL_GUID:
    if child_window != parent_GUID:
        driver.switch_to.window(child_window)
        driver.get("https://translate.google.com/")

        #back to parent
        driver.switch_to.window(parent_GUID)
        print('Parent window title is :' + driver.title)
#driver.close()