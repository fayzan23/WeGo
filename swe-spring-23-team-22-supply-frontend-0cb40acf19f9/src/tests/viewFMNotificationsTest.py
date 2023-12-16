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

class TestViewFMNotificationsTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_viewFMNotificationsTest(self):
    # Test name: viewFMNotificationsTest
    # Step # | name | target | value
    # 1 | open | https://swesupply2023team22.xyz/dashboard | 
    self.driver.get("https://swesupply2023team22.xyz/dashboard")
    # 2 | setWindowSize | 814x803 | 
    self.driver.set_window_size(814, 803)
    # 3 | click | css=.inboxIcon | 
    self.driver.find_element(By.CSS_SELECTOR, ".inboxIcon").click()
    # 4 | click | id=acknowledgeBtn | 
    self.driver.find_element(By.ID, "acknowledgeBtn").click()
    # 5 | click | css=.closeInbox | 
    self.driver.find_element(By.CSS_SELECTOR, ".closeInbox").click()
  
