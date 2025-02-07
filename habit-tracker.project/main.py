import requests, os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
username = "khisus19"
pixela_token = os.getenv("PIXELA_TOKEN")

user_params = {
    "token": pixela_token,
    "username": "khisus19",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)


graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": pixela_token
}

response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text)