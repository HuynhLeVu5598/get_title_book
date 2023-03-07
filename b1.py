from bs4 import BeautifulSoup
import os

name_file = "mylist.txt"


# Open the local HTML file
with open("synthetic.html", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Find all div elements with the specified class
divs_a = soup.find_all("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y")

# Loop through the divs and extract the content
list_content = []
for div_a in divs_a:
    # Check if the div_a is covered by divs_b or divs_c
    divs_b_c = div_a.find_parents(
        "div", class_=["a-row a-size-small", "a-size-small a-link-child"]
    )
    if divs_b_c:
        continue
    content = div_a.text.strip()
    list_content.append(content)


if not os.path.isfile(name_file):
    with open(name_file, "w", encoding="utf-8") as write_file:
        for ct in list_content:
            write_file.write(ct)
            write_file.write("\n")
else:
    with open(name_file, "a", encoding="utf-8") as write_file:
        for ct in list_content:
            print(ct)
            write_file.write(ct)
            write_file.write("\n")
