from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
import os

path = "C:/Users/BTTB/Downloads/*.epub"

driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://epub2pdf.io/")


# Send the file path to the file input element
for p in glob.glob(path):
    # Find the file input element
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(p)

    # Wait for the download button to become clickable
    download_button = WebDriverWait(driver, 100000).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
    )

    # Click the download button
    download_button.click()
    driver.refresh()
    os.remove(p)


# for p in glob.glob(path):
#     # Find the file input element
#     file_input = driver.find_element_by_xpath("//input[@type='file']")
#     file_input.send_keys(p)

#     # Wait for the download button to become clickable
#     download_button = WebDriverWait(driver, 100000).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
#     )

#     # Click the download button
#     download_button.click()
#     driver.refresh()
#     os.remove(p)
