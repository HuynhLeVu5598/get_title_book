from selenium import webdriver
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import glob
import pyautogui
import os

url = "https://accounts.google.com/ServiceLogin"

path = "D:/Vu/book/*.pdf"

with Chrome(use_subprocess=True) as driver:

    # driver = Chrome(use_subprocess=True)

    driver.get(url)

    #  ---------- EDIT ----------
    # email = "huynhlevumm@gmail.com"  # replace email
    # password = "100pagesCode3712"  # replace password
    #  ---------- EDIT ----------

    # sleep(2)
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.NAME, "identifier"))
    # ).send_keys(f"{email}\n")
    # sleep(2)
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.NAME, "Passwd"))
    # ).send_keys(f"{password}\n")

    sleep(40)

    driver.get("https://www.studypool.com/documents/sell/")
    sleep(2)

    login_link = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()
    sleep(2)

    login_button = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='btn-social btn-google']")
        )
    )
    login_button.click()
    sleep(2)

    for p in glob.glob(path):
        print(p)
        upload_button = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.btn-upload.dz-clickable")
            )
        )
        upload_button.click()

        file_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input.dz-hidden-input[type=file]")
            )
        )

        file_input.send_keys(p)
        sleep(2)

        # Press Alt + F4
        # pyautogui.hotkey("alt", "f4")
        sleep(4)

        okay_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "okay-btn"))
        )
        driver.execute_script("arguments[0].click();", okay_btn)
        sleep(20)
        os.remove(p)

        driver.refresh()

    sleep(1000)
