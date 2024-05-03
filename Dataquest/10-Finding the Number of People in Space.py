# https://app.dataquest.io/c/18/m/52/working-with-apis/10/finding-the-number-of-people-in-space?path=1&slug=data-analyst&version=1
"""
Learn

OpenNotify has one more API endpoint, astros.json. It tells us how many people are currently in space. You can find the format of the responses here.

Because we implement our own version of this API on our servers, this number will most likely be different from the current number (when you try to access the original API outside of Dataquest).
Instructions

    Find how many people are currently in space.

    Assign the result to in_space_count.
"""
# Call the API here.
import requests

response = requests.get("http://api.open-notify.org/astros.json")
json_data=response.json()
in_space_count=json_data.get('number',{})
print(in_space_count)