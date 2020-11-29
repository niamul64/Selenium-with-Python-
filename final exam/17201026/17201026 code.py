import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# first 3 test case should be faild # last 5 test cases should be passed
class SimpleTest(unittest.TestCase):
    def test1(self):# shoud not  pass
        #counting total check boxes

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()#clicking table dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/ul/li[3]/a').click()


        checkBoxes = self.driver.find_elements(By.TAG_NAME, "input")


        self.assertEqual(len(checkBoxes) , 6 , "matched")  # should not be passed it matched with 5

        self.driver.quit()



    def test2(self):# shoud not  pass


        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen


        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a').click()#clicking input form dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[1]/a').click()#clicking simple form demo
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/div/input').send_keys("Match")#inserting value at single input field
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button').click()#clicking show message

        self.assertNotEqual(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/div/span').text, "Match","message matched")  # should not be passed

        self.driver.quit()
    def test3(self):# shoud not  pass

        #clicking redio button
        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a').click()#clicking input forms
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/label[1]/input').click()#clicking redio button
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/p[2]/button').click()

        text=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/p[3]').text

        self.assertEqual(text , "Male")  # should not be passed

        self.driver.quit()

    def test4(self):# shoud not  pass


        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()#clicking table dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]').click()#clicking green

        checkBoxes = self.driver.find_elements(By.TAG_NAME, "input")


        self.assertEqual(len(checkBoxes) , 5 , "matched")  # should not  be passed

        self.driver.quit()



    def test5(self):# shoud  pass


        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen


        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a').click()#clicking input form dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[1]/a').click()#clicking simple form demo
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/div/input').send_keys("Match")#inserting value at single input field
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button').click()#clicking show message

        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/div/span').text, "Match","message matched")  # should be passed

        self.driver.quit()

    def test6(self):# shoud  pass


        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()#clicking table dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/ul/li[1]/a').click()#clicking table pagination


        #matching 1st row first columun value
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/section/div/table/tbody/tr[1]/td[2]').text,"Table cell", "matched")  # should be passed

        self.driver.quit()

    def test7(self):# shoud  pass


        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()#clicking table dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/ul/li[1]/a').click()#clicking table pagination


        #matching 1st row first columun value
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/section/div/table/tbody/tr[1]/td[2]').text,"Table cell", "matched")  # should be passed

        self.driver.quit()


    def test8(self):# shoud  pass

        #data searching test
        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('https://www.seleniumeasy.com/test/')

        time.sleep(10) #waiting for the popup screen
        self.driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click() # closing the popup screen




        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()#clicking table dropdown
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[3]/ul/li[2]/a').click()#clicking data search

        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys("bootstrap")#inserting value at single input field
        #matching 1st row first columun value
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]').text,"Bootstrap 3", "matched")  # should be passed

        self.driver.quit()







if __name__ == '__main__':
    unittest.main()