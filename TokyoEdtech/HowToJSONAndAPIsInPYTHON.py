# https://www.youtube.com/watch?v=YgO5ff9sp7A
# import json
# import requests
# from random import randint
#
# food_choice = input('Please enter your dinner choice: ')
# url = f"https://api.punkapi.com/v2/beers?food={food_choice}"
# r = requests.get(url)
#
# if r.status_code == 200:
#     data = json.loads(r.text)
#
#     beer_list = []
#
#     for beer in data:
#         name = beer['name']
#         tagline = beer['tagline']
#         abv = beer['abv']
#
#         beer_item = {
#             'name': name,
#             'tagline': tagline,
#             'abv': abv
#         }
#         beer_list.append(beer_item)
#
#     value = randint(0, len(beer_list))
#
#     try_this = beer_list[value]
#
#     try_name = try_this['name']
#     try_tagline = try_this['tagline']
#     try_abv = try_this['abv']
#
#     print(f"You should try {try_name}, {try_tagline}, {try_abv} %")


# --------------------------------------------

import json
import requests

d = {
    "Name1": {
        "NNum": "11",
        "Node1": {
            "SubNodeA": "Thomas",
            "SubNodeB": "27"
        },
        "Node2": {
            "SubNodeA": "ZZZ",
            "SubNodeD": "XXX",
            "SubNodeE": "yy"
        },
        "Node3": {
            "child1": 11,
            "child2": {
                "grandchild": {
                    "greatgrandchild1": "Rita",
                    "greatgrandchild2": "US"
                }
            }
        }
    }
}


def get_keys(d, curr_key=[]):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from get_keys(v, curr_key + [k])
        elif isinstance(v, list):
            for i in v:
                yield from get_keys(i, curr_key + [k])
        else:
            yield '.'.join(curr_key + [k])


print([*get_keys(d)])
