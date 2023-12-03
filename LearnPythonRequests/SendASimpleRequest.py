# Tuto https://en.git.ir/udemy-learn-python-requests/

import requests

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
r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)

with open('image.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)