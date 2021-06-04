import time
from selenium import webdriver

class ChromeDriverWindows:

    def searchGoogle(selfself):
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        driver.get("https://google.com")

        element = driver.find_element_by_id("L2AGLb")
        element.click()

        element_search = driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()

        #name="q"

        time.sleep(30)

        #L2AGLb



search = ChromeDriverWindows()
search.searchGoogle()