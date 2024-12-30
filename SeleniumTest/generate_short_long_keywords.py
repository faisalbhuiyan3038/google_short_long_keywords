from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Sample Test Case Started")

options = webdriver.EdgeOptions()

driver = webdriver.Edge(options=options)

driver.maximize_window()

driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("javatpoint")
search_box.send_keys(Keys.RETURN)
driver.close()

print("Sameple test case done")