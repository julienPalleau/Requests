# Tuto https://en.git.ir/udemy-learn-python-requests/

import requests

'''
Description
In this course you will learn about how requests on the web work and how to connect to APIs using the Python library called Requests. It covers everything you need to know about 
sending requests and handling responses in Python.

Why requests? Third-party APIs are a great way to add cool functionality to your app, and if you know how to access and use APIs, then you can take advantage of them. This course 
will help you get to the point where you're comfortable with working with APIs.

Check out list of videos that add up to over three hours below.

Join the course today by clicking the "Enroll in Course" button. I'll see you inside.
'''

# Doc: https://httpbin.org

###############################
# 1 - Intro                   #
# 2 - How Requests Work       #
# 3 - Setup                   #
# 4 - Documentation and Tools #
###############################

#############################
# 5 - Send A Simple Request #
#############################
# r = requests.get('https://enq8iajz8k4ce.x.pipedream.net

############################
# 6 - Reading The Response #
############################
'''
r = requests.get('https://reqres.in/api/users/2')
print(r.text)
json_data = r.json()
print(json_data['data']['first_name'])
'''

##############################
# 7 - Passing URL Parameters #
##############################
# r = requests.get('https://enq8iajz8k4ce.x.pipedream.net?key1=value1&key2=value2')
'''
payload = {'first': 'one', 'third': 'three'}
r = requests.get('https://enq8iajz8k4ce.x.pipedream.net', params=payload)
'''

######################
# 8 - Custom Headers #
######################
# Modifying Headers, most of the time you don't need it.
# However, common use case of modifying headers is passing a token (token is used for authentication)

'''
headers = {'my-token': '329uadnfag;jdfgajn8674jfaejdfdsfgnafgmnmthtimhg39'}
r = requests.get('https://enq8iajz8k4ce.x.pipedream.net', headers=headers)
'''

####################################
# 9 - Changing The Request Method #
###################################
# r = requests.post('https://enq8iajz8k4ce.x.pipedream.net')
# r = requests.delete('https://enq8iajz8k4ce.x.pipedream.net')
# r = requests.put('https://enq8iajz8k4ce.x.pipedream.net')
# r = requests.patch('https://enq8iajz8k4ce.x.pipedream.net')

###################################
# 10 Sending A Request with JSON #
##################################
'''
payload = {'name': 'Julien', 'job': 'Programmer'}
r = requests.post('https://enq8iajz8k4ce.x.pipedream.net', json=payload)
print(r.text)
'''

########################################
# 11 - Sending Request With Form Data #
#######################################
'''
payload = {
    'name': 'Julien',
    'location': 'Las Vegas'
}
# r = requests.post('https://enq8iajz8k4ce.x.pipedream.net', data=payload)
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

######################
# 12 - Sending Files #
######################
# '''
# files = {'file' : open('104.jpg', 'rb')}
# r = requests.post('https://enq8iajz8k4ce.x.pipedream.net', files=files)
# '''
# files = {'file': ('104.jpg', open('104.jpg', 'rb'), 'image/jpeg')}
# r = requests.post('https://enq8iajz8k4ce.x.pipedream.net', files=files)

########################
# 13 - Saving An image #
########################
# r = requests.get('https://httpbin.org/image/jpeg')
# print(r.headers)
#
# with open('image.jpg', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=500):
#         fd.write(chunk)

###################
# 14 - Exceptions #
###################
'''
Les codes les plus courants sont :

    200 : succès de la requête ;
    301 et 302 : redirection, respectivement permanente et temporaire ;
    401 : utilisateur non authentifié ;
    403 : accès refusé ;
    404 : ressource non trouvée ;
    500, 502 et 503 : erreurs serveur ;
    504 : le serveur n'a pas répondu.
    
more details @: https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP#Codes_d
'''
# r = requests.get('https://httpbin.org/status/505')
# print(r)
# => whatever code you put at the end 505, 205 whatever you'll print the code you put at the end of the url

'''
r = requests.get('https://httpbin.org/status/501')
# r.raise_for_status()
try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR! ERROR! ERROR!')
print(r)
'''
# # for the test we are using an url that doesn't exist
# try:
#     r = requests.get('https://dsklfjdslfudsfdsj.com')
# except requests.exceptions.ConnectionError:
#     print('CONNECTION ERROR!')

#################
# 15 - Timeouts #
#################
# try:
#     r = requests.get('https://httpbin.org/delay/10', timeout=5)
# except requests.exceptions.ReadTimeout:
#     print('TIMED OUT!!!')

##################################
# 16 - HTTP Basic Authentication #
##################################
from requests.auth import HTTPBasicAuth
r_wrong = requests.get('https://httpbin.org/basic-auth/user/passwd')
print(r_wrong)
r_right = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
print(r_right)

###################################
# 17 - Reading API Documentation #
##################################
# https://petstore.swagger.io/

#######################################
# 18 - API Documentation and Overview #
#######################################
# !!!!!!!!!!! Extremely important and usefull !!!!!!!!!! #
# https://restcountries.com/#rest-countries

'''
All
https://restcountries.com/v3.1/all

Name
Search by country name. If you want to get an exact match, use the next endpoint. It can be the common or official value
https://restcountries.com/v3.1/name/{name}
https://restcountries.com/v3.1/name/eesti
https://restcountries.com/v3.1/name/deutschland

Full Name
Search by country’s full name. It can be the common or official value
https://restcountries.com/v3.1/name/{name}?fullText=true
https://restcountries.com/v3.1/name/aruba?fullText=true

Code
Search by cca2, ccn3, cca3 or cioc country code (yes, any!)
https://restcountries.com/v3.1/alpha/{code}
https://restcountries.com/v3.1/alpha/co
https://restcountries.com/v3.1/alpha/col
https://restcountries.com/v3.1/alpha/170

List of codes
Search by cca2, ccn3, cca3 or cioc country code (yes, any!)
https://restcountries.com/v3.1/alpha?codes={code},{code},{code}
https://restcountries.com/v3.1/alpha?codes=170,no,est,pe

Currency
Search by currency code or name
https://restcountries.com/v3.1/currency/{currency}
https://restcountries.com/v3.1/currency/cop
Now you can search by how a citizen is called.
https://restcountries.com/v3.1/demonym/{demonym}
https://restcountries.com/v3.1/demonym/peruvian

Language
Search by language code or name
https://restcountries.com/v3.1/lang/{language}
https://restcountries.com/v3.1/lang/cop
https://restcountries.com/v3.1/lang/spanish

Capital city
Search by capital city
https://restcountries.com/v3.1/capital/{capital}
https://restcountries.com/v3.1/capital/tallinn

Calling code
In version 3, calling codes are in the idd object. There is no implementation to search by calling codes in V3.

Region
Search by region (replace X with the version you want to use)
https://restcountries.com/v3.1/region/{region}
https://restcountries.com/v3.1/region/europe

Subregions
You can search by subregions (replace X with the version you want to use)
https://restcountries.com/v3.1/subregion/{subregion}
https://restcountries.com/v3.1/subregion/Northern Europe

Translation
You can search by any translation name
https://restcountries.com/v3.1/translation/{translation}
https://restcountries.com/v3.1/translation/germany
https://restcountries.com/v3.1/translation/alemania
https://restcountries.com/v3.1/translation/Saksamaa

Filter Response
You can filter the output of your request to include only the specified fields.
https://restcountries.com/v3.1/{service}?fields={field},{field},{field}
https://restcountries.com/v3.1/all?fields=name,capital,currencies
'''