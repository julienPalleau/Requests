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
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1"
# }


headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
    "Accept": "image/jpeg"
}

response = requests.get("https://httpbin.org/image", headers=headers)
print("\n")
with open("myimage.jpg", "wb") as f:
    f.write(response.content)

import requests

response = requests.get('https://api.github.com/user', auth=('username', 'password'))

print(response.status_code)
print(response.content)

# Introduce a delay before you stop the request
response = requests.get("https://httpbin.org/delay/5", timeout=3)

res_json = response.json()
del res_json['origin']
print(res_json)