from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
driver.get('https://www.demoqa.com')


ele=driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div/div[2]')
ele.click()#clicking on Elements option


checkBox=driver.find_element(By.XPATH, '//*[@id="item-1"]')
checkBox.click()#clicking on checkBox option


home=driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/span/button')
home.click()#extract home option
for i in range(1,4):#extract options
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li['+ str(i)+']/span/button').click()

for i in range(1,3):#extract options
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li[2]/ol/li['+ str(i)+']/span/button').click()


#selecting Notes from desktop
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]').click()


#selecting Angular from documents
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()



# extra work
checkBoxes = driver.find_elements(By.TAG_NAME,"input" )
print("total check boxes="+str(len(checkBoxes)))

selected=0
not_selected=0
for i in checkBoxes:

    if i.is_selected()==False :
        not_selected+=1
        
    else:
        selected+=1
        
    
print("selected check boxes:"+str(selected))
print("not selected check boxes:"+str(not_selected))
# extra work end

time.sleep(8)
driver.quit()