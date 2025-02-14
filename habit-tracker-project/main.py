import requests, os, datetime

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

today = datetime.datetime.now()

pixel_request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=my_graph_endpoint, json=pixel_request_body, headers=headers)
# print(response.text)

##------------- Update a pixel (PUT REQUEST) -----------------##

new_date = datetime.datetime(2025, 2, 8)


update_pixel_request_body = {
    "quantity": "12",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.put(url=f"{my_graph_endpoint}/{new_date.strftime("%Y%m%d")}", json=update_pixel_request_body, headers=headers)
# print(response.text)


##------------- Delete a pixel (DELETE REQUEST) -----------------##
# Same endpoin as PUT
pixel_to_delete = datetime.datetime(2025, 2, 10)

delete_endpoint = f"{my_graph_endpoint}/{pixel_to_delete.strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)