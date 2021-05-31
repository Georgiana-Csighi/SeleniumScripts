import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from config.settings import URL

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path="D:\\chromedriver.exe")


class dragAndDrop():

    def testingDragAndDrop(self):
        driver.get(URL)

        pathIframe= driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)


        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(5)

        print("Am terminat")

dragAndDrop = dragAndDrop()
dragAndDrop.testingDragAndDrop()
driver.quit()









