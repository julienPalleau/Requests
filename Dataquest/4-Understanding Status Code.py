# https://app.dataquest.io/c/18/m/52/working-with-apis/4/understanding-status-codes?path=1&slug=data-analyst&version=1
'''
Learn

The request we just made returned a status code of 200. Web servers return status codes every time they receive an API request. A status code reports what happened with a request. Here are some codes that are relevant to GET requests:

    200 — Everything went okay, and the server returned a result (if any).
    301 — The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or when an endpoint's name has changed.
    401 — The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API.
    400 — The server thinks you made a bad request. This can happen when you don't send the information that the API requires to process your request (among other things).
    403 — The resource you're trying to access is forbidden, and you don't have the right permissions to see it.
    404 — The server didn't find the resource you tried to access.

Instructions

    Make a GET request to http://api.open-notify.org/iss-pass.

    Assign the status code of the response to status_code.

Answer
	response = requests.get("http://api.open-notify.org/iss-pass")
	status_code = response.status_code
'''
import requests
response = requests.get("http://api.open-notify.org/iss-now")
status_code = response.status_code
print(response.status_code)