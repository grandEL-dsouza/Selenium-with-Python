import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

driver = webdriver.Safari()
#driver = webdriver.Chrome('./chromedriver')
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)
upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()

file_name_element = driver.find_element(By.ID, "uploaded-files")
file_name = file_name_element.text

time.sleep(10)
driver.quit()
