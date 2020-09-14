from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path='C:/Sel_Firefox/geckodriver.exe')  #defining a driver variable to use the driver.exe in perfect path

#Today we will learn first about WebDriver Conditional Commands

#is_displayed() - boolean function to check if an element is displayed
#is_enabled() - boolean function to check if an element is enabled
#is_selected() - boolean function to check if a checkbox/radio button is selected or not

#send_keys() - to write on a text box



driver.get("https://scholar.google.com/")

#search bar finding out



articles = driver.find_element_by_xpath('//*[@id="gs_hp_sdt1"]') #radio button of ARTICLES
case = driver.find_element_by_xpath('//*[@id="gs_hp_sdt2"]')  #radio button of CASE LAW

time.sleep(3)

if case.is_selected() == False :
    time.sleep(2)
    case.click()
    time.sleep(2)
    s_box = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
    s_box.send_keys('murder')
    search = driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]')
    search.click()
    time.sleep(3)
    print(driver.title)

elif case.is_selected() == True :
    s_box = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
    s_box.send_keys('murder')
    search = driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]')
    search.click()
    print(driver.title)




#driver.get("https://www.upwork.com")

time.sleep(5)

driver.quit()