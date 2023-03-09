from selenium import webdriver
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def convert_string(string):
    # Replace all hyphens and underscores with spaces
    string = string.replace("-", " ").replace("_", " ")
    # Remove any remaining non-alphanumeric characters
    string = "".join(c for c in string if c.isalnum() or c.isspace())
    # Convert to lowercase and return
    return string.lower()


url = "https://accounts.google.com/ServiceLogin"


with Chrome(use_subprocess=True) as driver:

    # driver = Chrome(use_subprocess=True)

    driver.get(url)

    # email = "huynhlevumm@gmail.com"  # replace email
    # password = "100pagesCode3712"  # replace password

    # sleep(2)
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.NAME, "identifier"))
    # ).send_keys(f"{email}\n")
    # sleep(2)
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.NAME, "Passwd"))
    # ).send_keys(f"{password}\n")

    sleep(30)

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

    my_uploads_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='link' and contains(text(), 'My Uploads')]")
        )
    )
    my_uploads_link.click()

    # wait for the "td" element with class "text-right" to be visible
    td_element = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-right"))
    )

    # Find all <td class="text-right"> elements
    # td_elements = driver.find_elements(By.CSS_SELECTOR, "td.text-right")

    # Loop through each <td> element
    # for td in td_elements:

    while True:
        td_element = driver.find_element(
            By.CSS_SELECTOR, "td.text-right img.edit-error"
        ).find_element(By.XPATH, "..")
        if len(td_element.find_elements(By.CSS_SELECTOR, "img.edit-error")) == 0:
            break
        edit_btn = td_element.find_element(By.CSS_SELECTOR, "a.edit-btn")
        edit_btn.click()

        # Find the <input> element by ID
        input_element = driver.find_element(By.ID, "name")

        # Get the current value of the input field
        current_value = input_element.get_attribute("value")
        print(current_value)

        # driver.execute_script("window.open('');")
        driver.execute_script("window.open('about:blank', '_blank');")
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Open a URL in the new tab
        driver.get("https://www.google.com")
        sleep(3)
        # Wait until the search bar element is visible
        search_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )

        name = convert_string(current_value)
        print("name: ", name)

        # Type the search query and press Enter
        try:
            search_query = name + " site:amazon.com"
            search_bar.send_keys(search_query + Keys.RETURN)
            first_result = driver.find_element(
                By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md"
            )
            sleep(1)

            first_result.click()
            sleep(2)

            text_element = driver.find_element(By.ID, "productTitle")
            result_title = text_element.text

            # assuming 'driver' is your webdriver instance
            # element1 = driver.find_element(
            #     By.CSS_SELECTOR, 'a.a-link-normal[href*="field-author"]'
            # )
            # content1 = element1.text
            # result_title = result_title + " by " + content1

            # Print the title of the first search result
            print("Title: {}".format(result_title))
            sleep(1)

        except:
            try:
                driver.back()
                search_bar = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.NAME, "q"))
                )
                search_query = name + "amazon"
                search_bar.send_keys(search_query + Keys.RETURN)
                sleep(2)

                first_result = driver.find_element(
                    By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md"
                )
                sleep(1)

                first_result.click()
                sleep(2)

                text_element = driver.find_element(By.ID, "productTitle")
                result_title = text_element.text

                # assuming 'driver' is your webdriver instance
                # element1 = driver.find_element(
                #     By.CSS_SELECTOR, 'a.a-link-normal[href*="field-author"]'
                # )
                # content1 = element1.text
                # result_title = result_title + " by " + content1
                # Print the title of the first search result
                print("Title: {}".format(result_title))
                sleep(1)
            except:
                result_title = name

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # Clear the input field
        input_element.clear()

        # Enter new value in the input field
        input_element.send_keys(result_title)

        sleep(4)

        # # Wait for the button to be clickable and click it
        save_button = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.ID, "saveBtn"))
        )
        save_button.click()

        sleep(8)

    sleep(100000)
