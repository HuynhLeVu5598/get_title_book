from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver instance
driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")

# navigate to target webpage
driver.get("https://www.goodreads.com/list/popular_lists?page=1")

name_file = "goodreads9.txt"

book_titles = driver.find_elements(By.CLASS_NAME, "listTitle")

# book_titles = driver.find_elements(By.XPATH, "//a[@class='bookTitle']")

titles = []
# Print the titles
for title in book_titles:
    titles.append(title.text)

titles = titles[9:]
for tt in titles:
    sleep(5)
    element = driver.find_element(
        By.XPATH, f"//a[@class='listTitle' and contains(text(), '{tt}')]"
    )
    element.click()
    for i in range(98):

        # Find all elements with the specified tag
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        book_titles = driver.find_elements(By.XPATH, "//span[@itemprop='name']")

        for title in book_titles:
            mytitle = title.text
            with open(name_file, "a", encoding="utf-8") as write_file:
                write_file.write(mytitle)
                write_file.write("\n")

        sleep(2)

        # Find the element to click on
        next_link = driver.find_element(By.CSS_SELECTOR, 'a.next_page[rel="next"]')

        # Scroll to the element
        actions = ActionChains(driver)
        actions.move_to_element(next_link).perform()

        # Click on the element
        next_link.click()
        sleep(2)

    # driver.back()
