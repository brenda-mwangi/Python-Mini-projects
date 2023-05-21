import requests
import datetime
from test import tok
USERNAME = "brendamwangi"
TOKEN = tok

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": f"{TOKEN}",
    "username": f"{USERNAME}",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    "id":"test1",
    "name":"bathing graph",
    "unit":"commit",
    "type":"int",
    "color":"ajisai",
    "timezone": "Africa/Nairobi",
    }

header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
POST_endpoint = graph_endpoint +"/"+ graph_params["id"]

post_params = {
    "date": str(datetime.datetime.date(datetime.datetime.now())).replace("-",""),
    "quantity": "5"
    }

response = requests.post(url=POST_endpoint, json=post_params, headers=header)
print(response.text)
