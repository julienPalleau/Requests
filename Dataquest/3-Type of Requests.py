# https://app.dataquest.io/c/18/m/52/working-with-apis/3/types-of-requests?path=1&slug=data-analyst&version=1
'''
Learn

There are many different types of requests. The most common is a GET request, which we use to retrieve data.

We can use a simple GET request to retrieve information from the OpenNotify API.

OpenNotify has several API endpoints. An endpoint is a server route for retrieving specific data from an API. For example, the /comments endpoint on the reddit API might retrieve
information about comments, while the /users endpoint might retrieve data about users.

The first endpoint we'll look at on OpenNotify is the iss-now.json endpoint. This endpoint gets the current latitude and longitude position of the ISS. A dataset wouldn't be a
good tool for this task because the information changes often, and it involves some calculation on the server.

The endpoint we'll be working with is actually deprecated, but we have an archive of the original webpage and a mockup of the API available for use in the Dataquest interface, but
you won't be able to complete the same steps locally. Check out the complete list of active OpenNotify endpoints if you'd like to try the steps outlined in this lesson locally.

We've imported requests for you already, so you don't need to do it again in this lesson. Importing requests will overwrite some of the custom API logic we've developed for
answer-checking in this lesson.
Instructions

    The server will send a status code indicating the success or failure of your request. You can get the status code of the response from response.status_code.
        Assign the status code to the variable status_code.

Answer
	# Make a get request to get the latest position of the ISS from the OpenNotify API.
	response = requests.get("http://api.open-notify.org/iss-now.json")
	status_code = response.status_code
'''
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
print(status_code)