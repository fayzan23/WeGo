# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSignUpFormTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_signUpFormTest(self):
    # Test name: signUpFormTest
    # Step # | name | target | value
    # 1 | open | https://swesupply2023team22.xyz/signup | 
    self.driver.get("https://swesupply2023team22.xyz/signup")
    # 2 | setWindowSize | 1440x900 | 
    self.driver.set_window_size(1440, 900)
    # 3 | click | id=fName | 
    self.driver.find_element(By.ID, "fName").click()
    # 4 | type | id=fName | Taha
    self.driver.find_element(By.ID, "fName").send_keys("Taha")
    # 5 | type | id=lName | Lewis
    self.driver.find_element(By.ID, "lName").send_keys("Lewis")
    # 6 | type | id=email | testuser123@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("testuser123@gmail.com")
    # 7 | type | id=username | testuser1
    self.driver.find_element(By.ID, "username").send_keys("testuser1")
    # 8 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 9 | type | id=password | T3st!@#$
    self.driver.find_element(By.ID, "password").send_keys("T3st!@#$")
    # 10 | click | id=confirm-password | 
    self.driver.find_element(By.ID, "confirm-password").click()
    # 11 | type | id=confirm-password | T3st!@#$
    self.driver.find_element(By.ID, "confirm-password").send_keys("T3st!@#$")
    # 12 | click | id=togglePasswordSignUp | 
    self.driver.find_element(By.ID, "togglePasswordSignUp").click()
    # 13 | click | id=togglePasswordSignUp2 | 
    self.driver.find_element(By.ID, "togglePasswordSignUp2").click()
    # 14 | click | id=signUp | 
    self.driver.find_element(By.ID, "signUp").click()
  
