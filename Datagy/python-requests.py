# https://datagy.io/python-requests/

"""
Making HTTP GET Requests with the Python Requests Library

An HTTP GET request is used to retrieve data from the specified resource, such as a website. When using the Python requests library, you can use the .get() function to create a GET request for a specified resource.

The .get() function accepts two parameters:

    A url, which points to a resource, and
    params, which accepts a dictionary or tuples to send in the query string

Let’s see how we can use the get() function to make a GET request:
"""

# Making a GET Request with request.get()
import requests

resp = requests.get('https://reqres.in/api/users')
print(resp)