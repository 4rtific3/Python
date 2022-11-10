import requests
import datetime as dt

USERNAME = "johang"
TOKEN = "fda34fgyt"

today = dt.datetime.today()
date = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Water Drank",
    "unit": "litre",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# # Create new graph
# response = requests.post(url=post_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{post_graph_endpoint}/graph1"

pixel_config = {
    "date": date,
    "quantity": "2.5",
}

# # Create a new pixel
# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_pixel_date = "20221103"
put_pixel_endpoint = f"{post_pixel_endpoint}/{put_pixel_date}"

put_pixel_config = {
    "quantity": "3.2"
}

# Adjust the value of a pixel
response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
print(response.text)