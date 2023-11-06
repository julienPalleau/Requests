import requests

params = {
    "name": "Mike",
    "age": 25
}
url = "https://httpbin.org/get?name=Mike&age=25"
response = requests.get(url)
res_json = response.json()
del res_json['origin']
print(f'result of requests.get in json format response = requests.get("https://httpbin.org/get?name=Mike&age=25"): \n{res_json}')

response = requests.get(url, params=params)
print("\n")
print(f"url: \n{response.url}")
res_json = response.json()
del res_json['origin']
print("\n")
print(f"result of requests.get in json format but with a different request format response = requests.get(url, params=params): \n{res_json}")

payload = {
    "name": "Mike",
    "age": 25
}
# The post request
response = requests.post("https://httpbin.org/post", data=payload)
print("\n")
print(f"url: \n{response.url}")
res_json = response.json()
del res_json['origin']
print("\n")
print(f'result of requests.post in json format check the code response = requests.post("https://httpbin.org/post", data=payload): \n{res_json}')

# the error codes
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

# In the example below we create the error 404 and then we catch the error associated to 404 with requests.code
response = requests.get("https://httpbin.org/status/404")
if response.status_code == requests.codes.not_found:
    print("Not Found")
else:
    print(response.status_code)

response = requests.get("https://httpbin.org/status/401")
# In the example below we catch any error
# print(response.raise_for_status())


# User agent
response = requests.get("https://httbin.org/user-agent")
print("\n")
print(response.text)
