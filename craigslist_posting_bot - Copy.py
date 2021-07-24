from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import os.path




def find(browser):
    add_images = browser.find_element_by_xpath('//input[@name="file"]')
    if add_images:
        return add_images
    else:
        return False


browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

browser.get('https://post.craigslist.org/')

# Select Location
browser.find_element_by_class_name('ui-selectmenu-text').click()

browser.find_element_by_xpath('//li[@id="ui-id-532"]').click()

browser.find_element_by_xpath('//button[@name="go"]').click()


# Post Type Page
browser.find_element_by_xpath('//input[@name="id" and @value="fso"]').click()

# Category
browser.find_element_by_xpath('//input[@name="id" and @value="153"]').click()

# Main post page
title_area = browser.find_element_by_xpath('//input[@name="PostingTitle" and @id="PostingTitle"]')
title_area.send_keys('iPhone Repair In Roseville')

city = browser.find_element_by_xpath('//input[@name="geographic_area" and @id="geographic_area"]')
city.send_keys('Roseville, CA')

postal_code = browser.find_element_by_xpath('//input[@name="postal" and @id="postal_code"]')

postal_code.send_keys(95610)
time.sleep(1)

# main text section
main_text = browser.find_element_by_xpath('//textarea[@name="PostingBody" and @id="PostingBody"]')
main_text.send_keys('Check out our website for more information: https://mnmcomputers.com')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys('Hire an expert tech that you can trust with your iPhone! We perform screen repairs for all iPhone models with a low cost guarantee! We stand by our quality of our repairs and we guarantee we will make your device work like it’s brand new!')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys("$ Best iPhone Repair Prices in Town $")
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys('7613 Greenback Lane, Citrus Heights')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys("Please contact at 916-721-6677")




# Price
price = browser.find_element_by_xpath('//input[@name="price"]')
price.send_keys()


house_type = browser.find_element_by_xpath('//span[@id="ui-id-1-button"]').click()

actions = ActionChains(browser)

for x in range(4):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER).click()
actions.perform()

email = browser.find_element_by_xpath('//input[@name="FromEMail"]')
email.send_keys('nmedari@gmail.com')



# Select iOS

browser.find_element_by_class_name('mobile_os').click()

browser.find_element_by_xpath('//li[@id="ui-id-13"]').click()  

browser.find_element_by_xpath('//button[@class="go big-button submit-button"]').click()

# Find Location
street = browser.find_element_by_xpath('//input[@name="xstreet0" and @id="xstreet0"]')
street.send_keys('7613 Greenback Lane')
city_location = browser.find_element_by_xpath('//input[@name="city" and @id="city"]')
city_location.send_keys('Citrus Heights')

find_location = browser.find_element_by_xpath('//button[@id="search_button"]').click()
browser.find_element_by_xpath('//button[@class="continue bigbutton"]').click()
time.sleep(1)


# Send Pictures
browser.find_element_by_xpath('//a[@id="classic"]').click()

add_images = browser.find_element_by_xpath('//input[@name="file"]')

img = []
path = 'C:\\Users\\User\\Desktop\\clphotos'
valid_image = ['.jpg', '.gif', '.png', '.tga']
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_image:
        continue
    print(f)
    img.append(f'/clphotos/{f}')

for i in sorted(img):
    if add_images != False:
        print(os.getcwd() + i)
        add_images.send_keys(os.getcwd() + i)
        add_images = WebDriverWait(browser, 3).until(find)
    else:
        continue

browser.find_element_by_xpath('//button[@value="Done with Images"]').click()

# Phone number warning continue button

browser.find_element_by_xpath('//button[@value="continue"]').click()

#login

browser.find_element_by_link_text('log in').click()

username = browser.find_element_by_xpath('//input[@name="inputEmailHandle" and @id="inputEmailHandle"]')
username.send_keys('nmedari@gmail.com')

password = browser.find_element_by_xpath('//input[@name="inputPassword" and @id="inputPassword"]')
password.send_keys('Jay10192001$')

browser.find_element_by_xpath('//button[@id="login"]').click()

browser.find_element_by_xpath('//button[@name="go"]').click()