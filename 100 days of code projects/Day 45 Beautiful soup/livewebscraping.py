from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

anchor = soup.find_all(name="span", class_="titleline")
print(anchor)
