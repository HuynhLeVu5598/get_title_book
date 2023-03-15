from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
import time
import os

path = "C:/Users/BTTB/Downloads/*.azw3"

driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://ebook.online-convert.com/vi/convert/azw3-sang-pdf/")

for p in glob.glob(path):
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(p)

    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 100)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "convert_to")))

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    element.click()
    time.sleep(40)
    driver.refresh()
    # Click the "Convert Another File" button
    wait = WebDriverWait(driver, 1000)
    element0 = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "convert-another-file-to-text"))
    )
    element0.click()
    os.remove(p)

    print("-----")
