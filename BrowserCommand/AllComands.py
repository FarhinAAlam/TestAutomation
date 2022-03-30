from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#1 Open Browser

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#2 Close Browser

#driver.close()     eta holo single tab close er jonno

#driver.quit()  eta holo multiple tab ekbare close jnno
#3 full Screen
#driver.maximize_window()
#driver.fullscreen_window()
#4 open website

driver.get("https://www.google.com/")
#driver.close()

#5 set window size


#driver.set_window_size(768, 500)

#6 amar window size onojayi max ora bole dibe output e
#print(driver.set_window_size())

# 7 Tittle 0fweb page

title = driver.title
print( "Tittle is : " + title)

# 8  URL of current web page
url = driver.current_url
print("Url is : "  + url)


#9 Nabigation  ( back forward Refresh)
driver.get("https://www.opencart.com/")
driver.back()
print("After Back Title is " + driver.title)
driver.forward()
print("After forward Title is " + driver.title)

#10  Refresh
#driver.refresh()
