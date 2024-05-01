# https://app.dataquest.io/c/18/m/52/working-with-apis/5/hitting-the-right-endpoint?path=1&slug=data-analyst&version=1
'''
Learn

iss-pass wasn't a valid endpoint, so the API's server sent us a 404 status code in response. We forgot to add .json at the end, like the API documentation shows.
Instructions

    Make a GET request to http://api.open-notify.org/iss-now.json.

    Assign the status code of the response to status_code.

Answer
	response = requests.get("http://api.open-notify.org/iss-now.json")
	status_code=response.status_code
'''
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
print(status_code)