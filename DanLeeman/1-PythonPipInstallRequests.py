# https://www.youtube.com/watch?v=pEI6tQV6hsE&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=1

###############################
# Python Pip Install Requests #
###############################
# https://requests.readthedocs.io/en/latest/
# python -m pip install requests

###########
# Summary #
###########
# https://requests.readthedocs.io/en/latest/
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass')) # this is an example if you need to authenticate yourself
r = requests.get('https://api.github.com/user') # this is just to make the lines below to work

print(f"status code: {r.status_code}")
# 200

print(f"content-type: {r.headers['content-type']}")
# 'application/json; charset=utf8'

print(f"encoding: {r.encoding}")
# 'utf-8'

print(f"contenu du requests: \n{r.text}")
# '{"type":"User"...'

print(f"contenu au format jason: \n{r.json()}")
# {'private_gists': 419, 'total_private_repos': 77, ...}
