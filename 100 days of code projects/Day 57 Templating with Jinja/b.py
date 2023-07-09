import requests

url = "https://api.npoint.io/4152611fd8cc3f8b70c5"
data = requests.get(url).json()
print(data[1:])
