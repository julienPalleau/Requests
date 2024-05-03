# https://app.dataquest.io/c/18/m/52/working-with-apis/9/content-type?path=1&slug=data-analyst&version=1
"""
Working with APIs
9 of 11 · Content Type
Learn

The server sends more than a status code and the data when it generates a response. It also sends metadata with information on how it generated the data and how to decode it. This information appears in the response headers. We can access it using the .headers property.

The headers will appear as a dictionary. For now, the content-type within the headers is the most important key. It tells us the format of the response, and how to decode it. For the OpenNotify API, the format is JSON, so we were able to decode it with JSON earlier.
Instructions

    Get content-type from response.headers.

    Assign the content type to the content_type variable.

"""
# Headers is a dictionary
import requests

import requests
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

content_type = response.headers.get('content-type')
print(content_type)