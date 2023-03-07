from selenium import webdriver
import os
import time 

name_file = "synthetic.html"
driver = webdriver.Chrome("C:/Users/BTTB/Downloads/chromedriver_win32/chromedriver.exe")


driver.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_unv_books_1_1_1")

tech_category0 = driver.find_elements_by_css_selector("div._p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf._p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8")

all_link0 = []
for category0 in tech_category0:
    try:
        subcategories0 = category0.find_element_by_tag_name("a")
        link0 = subcategories0.get_attribute("href")
        all_link0.append(link0)

    except:
        pass


all_link0 = all_link0[-1:]
for al0  in all_link0:

    driver.get(al0)

    tech_category = driver.find_elements_by_css_selector("div._p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf._p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8")

    all_link = []
    for category in tech_category:
        try:
            subcategories = category.find_element_by_tag_name("a")
            link = subcategories.get_attribute("href")
            all_link.append(link)


        except:
            pass
        
    all_take_link = []
    for il in all_link: 

        if "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/" not in il:

            driver.get(il)  # click on the link and navigate to the new page

            time.sleep(2)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(4)

            html_content = driver.page_source
            print(html_content)


            if not os.path.isfile(name_file):
                with open(name_file, "w",encoding="utf-8") as write_file:
                    write_file.write(html_content)
                    write_file.write("\n")
            else:
                with open(name_file, "a",encoding="utf-8") as write_file:
                    write_file.write(html_content)
                    write_file.write("\n")

            # Find the page number 2 link and click it
            #page_2_link = driver.find_element_by_link_text('2')
            try:
                page_2_link = driver.find_element_by_xpath('//div[@class="a-text-center"]//a[text()="2"]')

                page_2_link.click()

                time.sleep(2)

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                time.sleep(4)

                with open(name_file, "a",encoding="utf-8") as write_file:
                    write_file.write(html_content)
                    write_file.write("\n")

                driver.back()
                
            except:
                pass
            
            driver.back()
