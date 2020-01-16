from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.eviebot.com/en/')
body = driver.find_element_by_class_name('stimulus')
body.send_keys('seleniumhq' )
# driver.get('https://google.com')


# driver.close()
