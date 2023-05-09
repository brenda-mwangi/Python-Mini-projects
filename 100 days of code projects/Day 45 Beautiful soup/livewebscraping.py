from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
print(response.text)

with open("news.html", 'w') as file:
    file.write(response.text)
