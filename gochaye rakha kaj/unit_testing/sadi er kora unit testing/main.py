from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


def send_data(self):
    driver = webdriver.Firefox(executable_path='D://Apps//Gecko//geckodriver.exe')
    driver.get("https://www.demoqa.com/text-box")

    fields = driver.find_elements(By.CLASS_NAME, "form-control")
    print(len(fields))

    given_name = 'MK Saadi'
    given_mail = "mksaadi@gmail.com"
    given_current_add = "Farmgate"
    given_perm_add = "Lalmatia"

    fields[0].send_keys(given_name)
    fields[1].send_keys(given_mail)
    fields[2].send_keys(given_current_add)
    fields[3].send_keys(given_perm_add)

    btn = driver.find_element_by_id("submit")
    btn.send_keys(Keys.RETURN)

    output = driver.find_elements_by_class_name("mb-1")

    found_name = output[0].text.split(':')[1]
    found_mail = output[1].text.split(':')[1]
    found_current_add = output[2].text.split(':')[1]
    found_perm_add = output[3].text.split(':')[1]
    return [found_name, found_mail, found_current_add, found_perm_add]



