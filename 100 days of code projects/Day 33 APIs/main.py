#working with APIs
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # returns a response code <Response [200]>
# print(response)

# returns a response code "200"
print(response.status_code)