# https://app.dataquest.io/c/18/m/52/working-with-apis/6/adding-query-parameters?path=1&slug=data-analyst&version=1
"""
Learn

In the last example, we got a 400 status code, which indicates a bad request. If we look at the documentation for the OpenNotify API, we see that the ISS Pass endpoint requires
two parameters.

The ISS Pass endpoint tells us when the ISS will pass over a given location on the Earth.

To request this information, we need to pass the coordinates for a specific location to the API. We do this by passing two parameters: latitude and longitude.

To do this, we can add an optional keyword argument, params, to our request. In this case, we need to pass in two parameters:

    lat — the latitude of the location
    lon — the longitude of the location

We can make a dictionary that contains these parameters, and then pass them into the function.

We can also do the same thing directly by adding the query parameters to the url, like this:

http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74

It's almost always better to set up the parameters as a dictionary, because the requests library we mentioned earlier takes care of certain issues, like properly formatting the
query parameters.

Instructions

    Use a dictionary and the parameters argument to get a response for latitude 37.78 and longitude -122.41 (the coordinates of San Francisco).

    Retrieve the content of the response with response.content.

    Assign the content to the variable content.
"""
# it doesn't work from PC but works from the web site.
import requests

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 37.78, "lon": -122.41}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

content=response.content
print(response.content)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-now.json?lat=40.71&lon=-74")
print(response.content)