from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
driver.get('https://www.demoqa.com')


ele=driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div/div[2]')
ele.click()#clicking on Elements option


txBox=driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]/span')
txBox.click()#clicking on TextBox option


Boxes = driver.find_elements(By.CLASS_NAME,"form-control" ) #find text boxes
print(len(Boxes)) #print how many text boxes are there 

#filling text boxs
Boxes[0].send_keys("Niamul Hasan")
Boxes[1].send_keys("niamulhassan64@gmail.com")
Boxes[2].send_keys("Puran Kochukhet, Dhaka Cant.,Dhaka-1206")
Boxes[3].send_keys("Puran Kochukhet, Dhaka Cant.,Dhaka-1206,Bangladesh")
#filling text boxs

time.sleep(8)
#submit box click
driver.find_element(By.XPATH, '//*[@id="submit"]').click()

time.sleep(8)

driver.quit()