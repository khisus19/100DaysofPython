import requests, os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "khisus19"
pixela_token = os.getenv("PIXELA_TOKEN")

##------------- Create a new user in Pixela -----------------##
user_params = {
    "token": pixela_token,
    "USERNAME": "khisus19",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)


##------------- Create a Graph in Pixela -----------------##
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": pixela_token,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


##------------- Post a pixel -----------------##
graphid = "graph1"
my_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graphid}"

pixel_request_body = {
    "date": "20250206",
    "quantity": "14",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=my_graph_endpoint, json=pixel_request_body, headers=headers)
print(response.text)