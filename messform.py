import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions

opts = FirefoxOptions()
driver = webdriver.Firefox(options = opts)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSed89CF0uApemSeT51htpGiNdzX6LTsjiBXecqpDRSXeycIfw/viewform')

email = driver.find_element_by_xpath('//*[@type="email"]')
email.send_keys("hello@gmail.com")

chbx = driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
xs = [2,3,4,5,7,8,11,12,16,18,26,27,30,34,36,37,38,39,40,48,51,53,55,56,58,59,61,62,64,65]
for i in xs:
	chbx[i].click()

submit = driver.find_element_by_xpath("//*[text() = 'Submit']")
submit.click()
driver.quit()
#jeha@netmail3.net
