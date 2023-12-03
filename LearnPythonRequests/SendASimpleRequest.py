# https://en.git.ir/udemy-learn-python-requests/

import requests

# r = requests.get('https://pipedream.com/@jpalleau/projects/proj_oLsD6e3/tree')
r = requests.get('https://reqres.in/api/users/2')
print(r.text)
json_data = r.json()
print(json_data['data']['first_name'])