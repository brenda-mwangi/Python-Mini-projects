import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
emperor_webpage = response.text

soup = BeautifulSoup(emperor_webpage, "html.parser")

movies = soup.find_all(name="h3")
print(movies)
