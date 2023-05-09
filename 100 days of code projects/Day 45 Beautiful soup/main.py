from bs4 import BeautifulSoup
with open("website.html", "rb") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")

# # print soup
# print(soup)

# # print prettified soup
# print(soup.prettify())

# # get the title
# print(soup.title)

# # get the title name
# print(soup.title.name)

# # get the title string
# print(soup.title.string)

# # gets the first a tag only
# print(soup.a)

# get all anchor (a) tags
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# for i in all_anchor_tags:
    # print(i.getText())
    # print(i.get('href'))

# all_H1 = soup.find(name='h3', class_='heading')
# print(all_H1)

# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name.getText())

# headings = soup.select(selector='.heading')
# print(headings)
