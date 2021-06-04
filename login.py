import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from config.settings import USERNAME, PASSWORD

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path="D:\\chromedriver.exe")


class TestingLogin():


    def LoginNOK(self , username, parola, testcase):

        driver.get("http://demo.guru99.com/V4/")

        user = driver.find_element(By.XPATH, "//input[contains(@name,'id')]")
        user.send_keys(username)

        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN" + testcase+ "NOK FAILED")
            else:
                print("TEST CASE LOGIN" + testcase+ "NOK PASS")
        except:
            print("TEST CASE LOGIN" + testcase+ " NOK PASS")




    def LoginOk(self, username, parola):

        #driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        driver.get("http://demo.guru99.com/V4/")

        #user = driver.find_element_by_name("uid")
        #user = driver.find_element_by_xpath("//input[@name='uid']")
        #user = driver.find_element(by.NAME, "uid")
        user = driver.find_element(By.XPATH, "//input[contains(@name,'id')]")


        user.send_keys(username)

        #password=driver.find_element_by_name("password")
        #password = driver.find_element_by_xpath("//input[@name='password']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN PASS")
            else:
                print("TEST CASE LOGIN FAILED")
        except:
            print("TEST CASE LOGIN FAILED")


test = TestingLogin()
test.LoginOk(USERNAME, PASSWORD)

#test.LoginNOK(username, parola)
test.LoginNOK( USERNAME, "parola NOK", "user ok, password nok")
test.LoginNOK(" user NOK", PASSWORD,  "user nok, passwor nok")
test.LoginNOK(" user NOK", "parola NOK",  "user nok, password nok")
test.LoginNOK("", "rehavAs",  "user <empty>, password ok")
test.LoginNOK( USERNAME, "",  "user ok, password <empty>")

driver.quit()
