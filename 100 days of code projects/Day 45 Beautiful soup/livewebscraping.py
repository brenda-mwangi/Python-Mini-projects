from bs4 import BeautifulSoup
import requests


response = requests.get("https://podfoods.co/")

# Parse HTML Code
soup = BeautifulSoup(response.content, 'html.parser')
yc_webpage = soup.prettify()

with open("food.html", "w") as food:
    food.write(yc_webpage)

