from selenium import webdriver

driver = webdriver.Chrome(executable_path = './chromedriver')
driver.get('https://web.whatsapp.com')

name =input('whom you want to send the message ')
message = input('what message you want to send ')
count = int(input('how many times you want to send the message '))

input('Press Enter after whatsapp loaded')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box =driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(message)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

print('process sucessfully finished')
driver.close()