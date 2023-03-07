from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
import time

path = "D:/Vu/djvu/*.djvu"

driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://ebook.online-convert.com/vi/convert/djvu-sang-pdf/")

for p in glob.glob(path):

    file_input = driver.find_element_by_xpath("//input[@type='file']")
    file_input.send_keys(p)

    # Submit the form
    # submit_button = driver.find_element_by_xpath("//input[@type='submit']")
    # submit_button.click()

    # Wait for the element to be clickable
    time.sleep(15)
    wait = WebDriverWait(driver, 1000)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "convert_to")))
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    time.sleep(40)
    driver.refresh()

    wait = WebDriverWait(driver, 1000)
    element0 = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "convert-another-file-to-text"))
    )
    element0.click()

    print("-----")
