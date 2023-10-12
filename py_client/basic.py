import requests

endpoint = 'http://localhost:8000/products'

get_response = requests.get(endpoint)
# get_response = requests.get(endpoint, params={"abc": 123}, json={'query': 'Hello'})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())


# Send the parameters in the query string
# params = {"abc": 123, "query": "Hello"}
# get_response = requests.get(endpoint, params=params)
#
# print(get_response.text)
# print(get_response.status_code)
