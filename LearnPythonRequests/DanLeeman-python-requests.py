# https://www.youtube.com/watch?v=qriL9Qe8pJc&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=2

import requests

###############
# GET REQUEST #
###############
payload = {"firstName": "John", "lastName": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)

# visualise the full complete url sent:
print(r.url)

# view the http response code
print(r.status_code)

# to view the response content from our url, we have a couple options. This will return the response body as bytes
print(f"r.content: {r.content}")

# Another option is to use r.text. This function will return the response body that is decode by the requests library based on the http headers passed in the http request.
print("\n")
print(f"r.text: {r.text}")


################
# POST REQUEST #
################
"""
Post requests are used most often when submitting data from a form or uploading files.
A post request is designed for creating or updating resources and allows larger amounts of content to be sent in a single request compared to a get request.
To convert our get request to a post request, there are just a few changes to be made.
"""