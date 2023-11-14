import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

driver = webdriver.Safari() #This line chooses the driver. Make sure either the driver is present in the same location and is correctly installed in the system.
#driver = webdriver.Chrome('./chromedriver')
driver.get("https://the-internet.herokuapp.com/upload") #This line in selenium goes to the Website / WebApp. Here is where we define the URL we want to test
time.sleep(5)
upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png")) #in case of the 'internet herokup app site' the upload file button expects an input. Hence No click action is performed here.
#note that in my case the file that I want to upload is required to be present in the Downloads folder. You can configure the same as per your preference.
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()

file_name_element = driver.find_element(By.ID, "uploaded-files")
file_name = file_name_element.text

time.sleep(10)
driver.quit()
