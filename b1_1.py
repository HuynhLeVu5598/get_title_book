from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

name_file = "gutenberg.txt"


# create webdriver instance
driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")

# navigate to target webpage
driver.get("https://www.gutenberg.org/ebooks/search/?sort_order=downloads")

while True:
    titles = driver.find_elements(By.CLASS_NAME, "title")
    for title in titles:
        mytitle = title.text
        with open(name_file, "a", encoding="utf-8") as write_file:
            write_file.write(mytitle)
            write_file.write("\n")

    # Find the "Next" button using the By class and click it
    next_button = driver.find_element(By.LINK_TEXT, "Next")
    next_button.click()

# close the browser window
sleep(100000)
