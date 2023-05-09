from bs4 import BeautifulSoup
with open("website.html", "rb") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
