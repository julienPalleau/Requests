# https://app.dataquest.io/c/18/m/52/working-with-apis/7/json-format?path=1&slug=data-analyst&version=1
'''
7 of 11 · JSON Format
Learn

You may have noticed that the API response we received earlier was a string. Strings are how we pass information back and forth through APIs, but it's not easy to get the
information we want out of them. How do we know how to decode the string we receive and work with it in Python?

Luckily, there's a format called JSON. (We mentioned it earlier in this lesson.) This format encodes data structures like lists and dictionaries as strings to ensure that
machines can read them easily. JSON is the main format for sending and receiving data through APIs.

Python offers great support for JSON through its json library. We can convert lists and dictionaries to JSON, and vice versa. Our ISS Pass data, for example, is a dictionary
encoded as a string in JSON format.

The JSON library has two main methods:

    dumps — takes in a Python object and converts it to a string
    loads — takes in a JSON string and converts it to a Python object

Instructions

    Use the JSON function loads to convert fast_food_franchise_string to a Python object.

    Assign the resulting Python object to fast_food_franchise_2.
'''
import requests

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the JSON library.
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

# convert fast_food_franchise)string back to dictionary
fast_food_franchise_2=json.loads(fast_food_franchise_string)
print(type(fast_food_franchise_2))