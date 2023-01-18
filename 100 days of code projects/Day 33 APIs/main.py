#working with APIs
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # returns a response code <Response [200]>
# print(response)

# returns a response code "200"
# print(response.status_code)

# # raise error for the status code
# if response.status_code == 400:
#     raise Exception("Does not exist")
# elif response.status_code == 401:
#     raise Exception("Not authorized.")

# response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(data)
print(iss_position)