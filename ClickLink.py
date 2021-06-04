import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config.settings import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options,executable_path=CHROME_PATH)

class TestingClickLink():

    def clickLink(self):

        driver.get(URL)

        links = driver.find_elements_by_link_text("click here")
        for onelink in links:
            att = onelink.get_attribute('href')
            if att == "http://www.fb.com/":
                onelink.click()
                title = driver.title
                if "Facebook" in title:
                    print("Found")
                break

test = TestingClickLink()
test.clickLink()

driver.quit()
