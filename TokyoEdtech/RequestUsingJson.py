# https://www.youtube.com/watch?v=q30GEwUe5gY
"""
How to Acccess Web APIs using Python Requests and JSON.
json means Java Script Object Notation
Let's look at using the request module and json module to do web api(application programming interface) requests.
The website that we're going to interact with is called tvmaze.com and they have information about tv programs.
The goal is to connect to tv maze api (https://www.tvmaze.com/api).
Let's start with "Show single search"(https://www.tvmaze.com/api#show-single-search)
So here is the URL (/singlesearch/shows?q=:query)
"""

import requests
import json
import pprint

url = "https://api.tvmaze.com/singlesearch/shows"
show = input("Please input a show name. > ")
"""
params, note you can call whatever you want, but the convention is to use params.
The example on the web page is:  https://api.tvmaze.com/singlesearch/shows?q=girls
"""
params = {"q": show}

response = requests.get(url, params)

"""
We have to remember that the lines belows return text even if it looks like a python dictionary it is acturally text.
"""
if response.status_code == 200:
    data = json.loads(response.text)
    # pprint.pprint(data)

    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print(f"{name} premiered on {premiered}.")
    print(summary)
else:
    print(f"Error: {response.status_code}")

"""
Let's convert this text into a python dictionary which is surprisingly straightforward. To do that i'm going to go import json.
So this line data = json.loads(response.text) will take response.text and will transform it in data dictionary.
"""


