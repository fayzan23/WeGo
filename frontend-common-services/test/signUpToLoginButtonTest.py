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

class TestSignUpToLoginButtonTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_signUpToLoginButtonTest(self):
    # Test name: signUpToLoginButtonTest
    # Step # | name | target | value
    # 1 | open | https://swe2023team22.xyz/signup | 
    self.driver.get("https://swe2023team22.xyz/signup")
    # 2 | setWindowSize | 1039x803 | 
    self.driver.set_window_size(1039, 803)
    # 3 | click | id=directLogIn | 
    self.driver.find_element(By.ID, "directLogIn").click()
  