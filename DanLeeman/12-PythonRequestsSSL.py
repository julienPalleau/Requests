# https://www.youtube.com/watch?v=lfqG4q8hVew&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=9

#####################
# PythonRequestsSSL #
#####################
"""
SSL stands for Secure Socket Layers which is a protocol used by SSL certificates to initiate secure sessions with a browser.
SSL certificates are small data files that use a public key infrastructure to make internet transactions secure when using https protocol.
When a client connects to a server secured with SSL, the secured server will send back an encrypted publick key and a certificate.
The client will then check the certificate and if it is trusted, the client will create an encrypted key using the servers's public key and send the new key to the server.
Lastly, the server will decrypt the new key using the server's private key and then send an aknowledgement to the client that is encrypted with the new key created by the client.
Now the server and the client can encrypt all transmissions with the new key.
To work with SSL certificates using the Requests library, we will start a new script with Requests imported.
By default, the Requests library verifies SSL certificates the same way browser does, and if the SSL certificate is not verified, the Requests library will throw an SSLError.
We will create a new response object r and set this equal to requests.get() Within the get function we will add the url https://github.com/ which has SSL configured.
If we wanted to provide a list of trusted CAs to use to verify the request, we could use the verify keyword and provide a path to the directory where the CAs stored.
A trusted CA, or Certificate Authority, is a trusted entity that issues digital certificates which certifies the owner of a public key.
We can also provide a list of CAs when using a session by declaring a new session variable s and setting this equal to requests.Session(). Now we will call the verify function on
the session objects and specify the path to our directory with certificates of trusted CAs.
If we want the Requests library to ignore verifying the SSL certificate, we can set the verify keyword within a request to False.
"""
import requests

s = requests.Session()
s.verify = 'path/to/CAs'
r = requests.get('https://github.com', verify='path/to.CAs')
r = requests.get('https://github.com', verify=False)