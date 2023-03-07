
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

with open("mylistunique.txt", "r",encoding="utf-8") as read_file:
    content = read_file.readlines()

text = ""
for c in content:
    text += c

sentences = text.split("\n")

# Open the web page in a browser
driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")

# Loop through the sentences and open a new tab for each one
for sentence in sentences:
    if len(sentence) >= 3:

        # Open a new tab
        #driver.execute_script("window.open('');")
        driver.execute_script("window.open('about:blank', '_blank');")
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        # Go to the search page
        driver.get("https://libgen.is/")
        # Find the input field by ID and set its value
        input_element = driver.find_element_by_id("searchform")
        input_element.clear()
        input_element.send_keys(sentence)
        # Find the submit button by its type attribute
        submit_button = driver.find_element_by_xpath("//input[@type='submit']")
        # Click the button
        submit_button.click()

        # # Try to get the download link, close the tab if not found
        try:
            download_link = driver.find_element_by_xpath("//a[@title='this mirror']")
            #print(download_link.get_attribute("href"))
            download_link.click()


            get_link = driver.find_element_by_partial_link_text("GET")
            get_link.click()

            if driver.find_elements_by_xpath("//h1[contains(text(), '503 Service Temporarily Unavailable')]"):

                driver.back()
                try:
                    cloudflare_link = driver.find_element_by_partial_link_text("Cloudflare")
                    cloudflare_link.click()
                except:
                    pass

        except NoSuchElementException:
            pass
        
        # Switch to the currently active window
        driver.switch_to.window(driver.window_handles[-1])
        # Close the current window
        driver.close()
        # Switch back to the original window
        driver.switch_to.window(driver.window_handles[0])

        #     get_link = driver.find_element_by_partial_link_text("GET")
        #     get_link.click()

        # except NoSuchElementException:
        #     # Switch to the currently active window
        #     driver.switch_to.window(driver.window_handles[-1])
        #     # Close the current window
        #     driver.close()
        #     # Switch back to the original window
        #     driver.switch_to.window(driver.window_handles[0])
        