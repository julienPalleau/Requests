# https://www.youtube.com/watch?v=b_D-QvqmX3k&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=11

#######################
# PythonRequestsProxy #
#######################
import requests

params = {
    "name": "Mike",
    "age": 25
}
url = "https://httpbin.org/get?name=Mike&age=25"
response = requests.get(url)
res_json = response.json()
del res_json['origin']
print(res_json)

response = requests.get(url, params=params)
print(response.url)
res_json = response.json()
del res_json['origin']
print(res_json)

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
print(response.raise_for_status())


# User agent
import requests
response = requests.get("https://httbin.org/user-agent")
print(response.text)
