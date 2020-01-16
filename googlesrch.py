from selenium import webdriver
from selenium.webdriver.common import keys



driver = webdriver.Chrome(executable_path = './chromedriver')
driver.get('https://google.com')
search = driver.find_element_by_class_name('gLFyf')
search.send_keys('jusper')
search.submit()
# try:
#     links = driver.find_element_by_class_('LC20lb')
#except:
    #links = driver.find_element_by_xpath("//h3//a")

links = driver.find_element_by_xpath("//h3//a")

# result =[]
# for links in range(5):
#     href = links.get_attribute("href")
#     result.append(href)


print(links)
driver.close()
print('sucessfully finished')


# list1 = ['something','everything','letter','better']

# for item in range(len(list1)):
#     print(item)
