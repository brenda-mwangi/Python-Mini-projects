import requests

url = 'https://api.npoint.io/4152611fd8cc3f8b70c5'

num=1
response= requests.get(url).json()[num]

print(response)
