"""
Working with APIs: Takeaways
by Dataquest Labs, Inc. - All rights reserved © 2023

Syntax
    + Accessing the content of the data the server returns:
        response.content
    + Importing the JSON library:
        import json
    + Getting the content of a response as a Python object:
        response.json()
    + Accessing the information on how the server generated the data, and how to decode the data:
        response.headers

Concepts
    + An application program interface (API) is a set of methods and tools that allows differentapplications to interact. Web servers host APIs.
    + Programmers use APIs to retrieve data as it becomes available, which allows the client to quickly and effectively retrieve data that changes frequently.
    + JavaScript Object Notation (JSON) format is the primary format for sending and receiving datathrough APIs. JSON encodes data structures like lists and dictionaries as
      strings so machines can read them easily.
    + The JSON library has two main methods:
        •dumps — takes in a Python object and converts it to a string.
        •loads — takes in a JSON string and converts it to a Python object.
    + We use the requests library to communicate with the web server and retrieve the data.•An endpoint is a server route for retrieving specific data from an API.
    + Web servers return status codes every time they receive an API request.•Status codes that are relevant to GET requests:
        •200 — everything went okay, and the server returned a result.
        •301 — the server is redirecting you to a different endpoint. This can happen when acompany switches domain names or an endpoint's name has changed.
        •400 — the server thinks you made a bad request. This can happen when you don't sendthe information the API requires to process your request.
        •401 — the server thinks you're not authenticated. This happens when you don't supplythe correct credentials.
        •403 — the resource you're trying to access is forbidden, and you don't have the rightpermissions to see it.
        •404 — the server didn't find the resource you tried to access.

Resources
    •https://docs.python-requests.org/en/latest/
    •https://docs.python.org/3.6/library/json.html
"""