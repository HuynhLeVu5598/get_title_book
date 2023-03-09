# <div role="treeitem" class="_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8">
# <a href="/Best-Sellers-Books-Arts-Photography/zgbs/books/1/ref=zg_bs_nav_books_1">Arts &amp; Photography</a></div>


# from selenium import webdriver
# import os

# name_file = "synthetic.html"
# driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")
# driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_unv_books_1_1_1")

# tech_category = driver.find_elements_by_css_selector("div._p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf._p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8")

# all_link = []
# for category in tech_category:
#     try:
#         subcategories = category.find_element_by_tag_name("a")
#         link = subcategories.get_attribute("href")
#         print(link)
#         all_link.append(link)

#     except:
#         pass


# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from selenium import webdriver
# # define the driver and navigate to the page
# driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")

# driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_unv_books_1_1_1")

# # wait for some time to let the page load
# time.sleep(2)


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# time.sleep(2)

# html_content = driver.page_source
# with open("test.html", "w", encoding="utf-8") as file:
#     file.write(html_content)


# # Find the page number 2 link and click it
# page_2_link = driver.find_element_by_link_text('2')
# page_2_link.click()

# time.sleep(2)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# time.sleep(2)


# with open("test.txt", "r",encoding="utf-8") as read_file:
#     content = read_file.readlines()

# mycontent = ""
# for c in content:
#     mycontent += c
# print(mycontent)


# def remove_duplicates(text):
#     # Tách các câu thành danh sách
#     sentences = text.split("/n")
#     # Sử dụng set để loại bỏ các câu trùng lặp
#     unique_sentences = list(set(sentences))
#     unique_list = []
#     errors = ["®","Vol"]
#     for title in unique_sentences:
#         for error in errors:
#             if error in title:
#                 if len(title.split(error)[0]) >5:
#                     title = title.split(error)[0].strip()
#             else:
#                 title = title.strip()

#         unique_list.append(title)
#     unique_list = list(set(unique_list))

#     # Gộp lại các câu không trùng lặp thành một chuỗi
#     unique_text = "/n".join(unique_list)
#     return unique_text

# mytext = remove_duplicates(mycontent)
# print(mytext)

# with open("test1.txt", "w",encoding="utf-8") as write_file:
#     for ct in mytext:
#         write_file.write(ct)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-setuid-sandbox')

# driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)

# driver.get('chrome://settings/downloads')

# # find the button element
# # button = driver.find_element_by_xpath('//cr-button[text()="Change"]')
# # change_button = driver.find_element_by_xpath("//cr-button[normalize-space()='Change']")
# # change_button.click()


# # Find the element by tag name and text
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//cr-button[contains(text(), "Change")]'))
# )

# # Click on the element
# element.click()


# # button.click()

# # change_button.send_keys("C:/Users/BTTB/Downloads/book")


# # Find the element by tag name and text
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//cr-button[contains(text(), "Change")]'))
# )

# # Click on the element
# element.click()

# # Wait for the page to load completely
# driver.implicitly_wait(10)

# # Close the browser window
# driver.quit()


# from selenium import webdriver
# from undetected_chromedriver import Chrome
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import glob
# import pyautogui

# url = "https://accounts.google.com/ServiceLogin"

# path = "C:/Users/BTTB/Downloads/abc/*.pdf"

# with Chrome(use_subprocess=True) as driver:

#     # driver = Chrome(use_subprocess=True)

#     driver.get(url)

#     #  ---------- EDIT ----------
#     email = "huynhlevumm@gmail.com"  # replace email
#     password = "100pagesCode3712"  # replace password
#     #  ---------- EDIT ----------

#     sleep(2)
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.NAME, "identifier"))
#     ).send_keys(f"{email}\n")
#     sleep(2)
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.NAME, "Passwd"))
#     ).send_keys(f"{password}\n")

#     sleep(10)

#     driver.get("https://www.studypool.com/documents/sell/")

#     login_link = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
#     )
#     login_link.click()

#     login_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//button[@class='btn-social btn-google']")
#         )
#     )
#     login_button.click()

#     for p in glob.glob(path):

#         upload_button = WebDriverWait(driver, 100).until(
#             EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "div.btn-upload.dz-clickable")
#             )
#         )
#         upload_button.click()

#         # Wait for the file upload dialog to appear
#         dialog = WebDriverWait(driver, 100).until(
#             EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "input.dz-hidden-input[type=file]")
#             )
#         )

#         # Click on the close button using pyautogui
#         close_button_position = pyautogui.locateCenterOnScreen("close_button.png")
#         pyautogui.click(close_button_position)

#         # Wait for the dialog to disappear
#         WebDriverWait(driver, 100).until_not(
#             EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "input.dz-hidden-input[type=file]")
#             )
#         )

#         okay_btn = WebDriverWait(driver, 300).until(
#             EC.presence_of_element_located((By.ID, "okay-btn"))
#         )
#         okay_btn.click()

#         sleep(2)


# from datetime import datetime

# flag = True
# while flag:
#     print("Nhap ngay thang nam: ", end=" ")
#     datetime_str = str(input())
#     try:
#         datetime_object = datetime.strptime(datetime_str, "%d/%m/%y").date()
#         flag = False
#         print(type(datetime_object))

#     except:
#         print("Nhap sai")
#         pass

# from time import sleep

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import glob


# def convert_string(string):
#     # Replace all hyphens and underscores with spaces
#     string = string.replace("-", " ").replace("_", " ")
#     # Remove any remaining non-alphanumeric characters
#     string = "".join(c for c in string if c.isalnum() or c.isspace())
#     # Convert to lowercase and return
#     return string.lower()


# path = "D:/Vu/a/*.pdf"


# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")


# for p in glob.glob(path):

#     # driver.execute_script("window.open('');")
#     driver.execute_script("window.open('about:blank', '_blank');")
#     # Switch to the new tab
#     driver.switch_to.window(driver.window_handles[-1])

#     # Open a URL in the new tab
#     driver.get("https://www.google.com")
#     sleep(1)
#     # Wait until the search bar element is visible
#     search_bar = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.NAME, "q"))
#     )

#     index = 0
#     for i, a in zip(reversed(range(len(p))), reversed(p)):
#         if a == "\\":
#             index = i
#             break

#     name = p[index + 1 : -4]

#     name = convert_string(name)
#     print("name: ", name)

#     # Type the search query and press Enter
#     try:
#         search_query = name + " site:amazon.com"
#         search_bar.send_keys(search_query + Keys.RETURN)
#         first_result = driver.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")

#     except:
#         driver.back()
#         search_bar = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, "q"))
#         )
#         search_query = name
#         search_bar.send_keys(search_query + Keys.RETURN)
#         sleep(2)

#         first_result = driver.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")

#     sleep(1)

#     first_result.click()
#     sleep(2)

#     text_element = driver.find_element(By.ID, "productTitle")
#     result_title = text_element.text

#     # Print the title of the first search result
#     print("Title: {}".format(result_title))
#     sleep(1)

#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])

#     sleep(1)


# sleep(1000)

from selenium import webdriver
from selenium import webdriver
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.amazon.com/Lonely-Planet-Munich-Bavaria-Forest/dp/1788680510")

element1 = driver.find_element(By.CSS_SELECTOR, 'a.a-link-normal[href*="field-author"]')
content1 = element1.text
print(content1)
