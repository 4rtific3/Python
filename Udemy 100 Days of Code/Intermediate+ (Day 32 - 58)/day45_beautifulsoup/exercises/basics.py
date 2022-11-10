from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as df:
    data = df.read()

soup = BeautifulSoup(data, "html.parser")

# # Printing an indented copy of the code
# print(soup.prettify())

# # Printing the first tag found in the code
# print(soup.title)

# Printing all the tags in a list
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# # Printing the items contained within all tags in a list
# for tag in all_anchor_tags:
#     # Printing the text
#     print(tag.getText())
#     # Printing the href
#     print(tag.get("href"))
    
# Search by attribute name
# # Search by id
# heading = soup.find(name="h1", id="name")
# print(heading)

# # Search by class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# # Search by selector
# company_url = soup.select_one(selector="p a")
# print(company_url)