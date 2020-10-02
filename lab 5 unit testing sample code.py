import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SimpleTest(unittest.TestCase):
    driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
    driver.get('https://demoqa.com/text-box')
    def test1(self):

        Boxes = self.driver.find_elements(By.CLASS_NAME, "form-control")  # find text boxes

        # filling text boxs
        Boxes[0].send_keys("Niamul Hasan")
        Boxes[1].send_keys("niamulhassan64@gmail.com")
        Boxes[2].send_keys("Puran Kochukhet, Dhaka Cant.,Dhaka-1206")
        Boxes[3].send_keys("Puran Kochukhet, Dhaka Cant.,Dhaka-1206,Bangladesh")
        # filling text boxs
        time.sleep(3)

        # submit box click
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="name"]').text, "Name:Niamul Hasan","Name Matched") # should be passed
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="email"]').text, "Email:niamulhassan64@gmail.com", "email matched")  # should be passed

        self.assertEqual(self.driver.find_element(By.XPATH, '/ html / body / div / div / div / div[2] / div[2] / div[1] / form / div[6] / div / p[3]').text, "Current Address :Puran Kochukhet, Dhaka Cant.,Dhaka-1206")  # should be passed
        self.assertEqual(self.driver.find_element(By.XPATH,'/ html / body / div / div / div / div[2] / div[2] / div[1] / form / div[6] / div / p[4]').text, "Permananet Address :Puran Kochukhet, Dhaka Cant.,Dhaka-1206,Bangladesh" )


        self.driver.quit()



if __name__ == '__main__':
    unittest.main()