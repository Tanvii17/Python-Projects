import requests
from datetime import datetime

today = datetime.now()

USERNAME = "[Username of pixela account]"
TOKEN = "[Token given on account]"
ID = "graph1"
DATE = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "[Whatever your habit you want to track - Type name for that ,here]",
    "unit": "min",
    "type": "float",
    "color": "sora",

}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

pixel_params = {
    "date": DATE,
    "quantity": input("How many [minutes/hours (Based on your habit)] did you meditate today?"),

}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(response.text)

update_request_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"

update_params = {
    "quantity": "70.0"
}

# response = requests.put(url=update_request_endpoint, json=update_params, headers=header)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"

# response = requests.delete(url=delete_pixel_endpoint, headers=header)
# print(response.text)

### Uncomment some of the above lines if you want to put something in pixela, post or delete something.
