# https://app.dataquest.io/c/18/m/52/working-with-apis/8/getting-json-from-a-request?path=1&slug=data-analyst&version=1
"""
Learn

We can get the content of a response as a Python object by using the .json() method on the response.
Instructions

    Get the duration value of the ISS's first pass over San Francisco and assign the value to first_pass_duration.
"""

# Make the same request we did two screens ago.
import requests
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)
print("1")
print(json_data['response'])
first_pass_duration = json_data.get('response',{})[0].get('duration')
