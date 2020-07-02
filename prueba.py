from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome("C:\GeckoDriver\chromedriver.exe")

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary,
                           executable_path=r'C:\\GeckoDriver\\geckodriver.exe')


driver.get('https://mobile.facebook.com/')
print("Opened facebook...")

time.sleep(2)

init_ = driver.find_element_by_xpath(
    "//a[@class='_54k8 _56bs _4n43 _6gg6 _901w _56bu _52jh' or @class='be bf bg bh bi bj bk']")
init_.click()
email = driver.find_element_by_xpath(
    "//input[@id='m_login_email' or @name='email']")
email.send_keys()
print("email entered...")
password = driver.find_element_by_xpath(
    "//input[@id='pass' or @name='pass']")
password.send_keys()
print("Password entered...")
button = driver.find_element_by_xpath("//button[@name='login']")

time.sleep(3)

button.click()
print("facebook opened")
count = 0
while count < 158:
    print(count)
    time.sleep(2)
    status = driver.find_element_by_xpath(
        "//textarea[@id='composerInput']")
    status.send_keys('.')
    print("Status trying")
    time.sleep(1)
    button2 = driver.find_element_by_xpath("//button[@name='submit']")
    button2.click()
    print("post done")
    count += 1

# elements = driver.find_elements_by_class_name("_1mf _1mj")

# # status = driver.find_elements_by_xpath("// *[@class ='notranslate _5rpu\
# #                                                uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\
# #                                                inlineReplyTextArea mentionsTextarea textInput']")

# # status = driver.find_element_by_class_name(
# #     "//form[contains(@class,' _129h')]//div[contains(@class,' _3d2q _7c_r _4w79')]//div[contains(@class,'_5rp7')]//div[contains(@class,'_5rpb')]//div[contains(@class,'notranslate _5rpu')]//div//div[contains(@class,'')]//div[contains(@class,'_1mf _1mj')]")

# print(elements)

# feed = 'Hello!'
# cnt = 0

# for el in elements:
#     cnt += 1
#     element_id = str(el.get_attribute('id'))
#     XPATH = '//*[@id ="' + element_id + '"]'
#     post_field = driver.find_element_by_xpath(XPATH)
#     post_field.send_keys(feed)
#     post_field.send_keys(Keys.RETURN)
#     print("Comment" + str(cnt))

# # status.send_keys("Hola Mundo!:'v")
# # print("Status trying")

# # # postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
# # postbutton = driver.find_element_by_xpath(
# #     "//div[@contenteditable='true']").sendKeys("Hello World")
# # # postbutton.click()


# # /form[contains(@class,' _129h')]/div[contains(@class,' _3d2q _7c_r _4w79')]/div[contains(@class,'_5rp7')]/div[contains(@class,'_5rpb')]/div[contains(@class,'notranslate _5rpu')]/div[]/div[contains(@class,'')]/div[contains(@class,'_1mf _1mj')]


# # driver.findElement(By.xpath(
# #     "//ul[@class='UFIList']/div[contains(@id,'addComment')]//div[@class='UFICommentContainer']//div[contains(@class,'UFIAddCommentInput')]"))
# # ("//div[@contenteditable='true']")).sendKeys("Hello World")
