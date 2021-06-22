"""
REQUEST:
-Standard library to make HTTP request
-Response content will be a serialized JSON content

HTTP NOTES:
-Methods:
    -GET     -> request data from a specified resource
    -POST    -> send data to a server to modify and update a resource
    -PUT     -> send data to a server to create a resource or overwrite it
    -HEAD    -> request data from a specified resource without the response body
    -DELETE  -> delete the specified resource
    -OPTIONS -> describe the communication options for the target resource
-Status codes:
    -200 -> status OK
    -404 -> not found
-Query string:
    -+ -> represent a space in query string
    -& -> separate the various var=value pairs in the query string
-Sessions
    -Because HTTP is stateless, in order to associate a request to any other request, you need a way to store user data
    between HTTP requests.
    -Cookies or URL parameters (for ex. like http://example.com/myPage?asd=lol&boo=no) are both suitable ways to
    transport data between 2 or more request. However they are not good in case you don't want that data to be
    readable/editable on client side.
    -The solution is to store that data server side, give it an "id", and let the client only know (and pass back at
    every http request) that id. There you go, sessions implemented. Or you can use the client as a convenient remote
    storage, but you would encrypt the data and keep the secret server-side.
    -Of course there are other aspects to consider:
        *you don't want people to hijack other's sessions.
        *you want sessions to not last forever but to expire.
"""

import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout



# -----------------GET REQUEST-----------------

# Retrieve data from a specified resource with get()
response = requests.get('https://api.github.com')

# Timeout your request
# timeout=n      -> wait n seconds before timeout
# timeout=(n, m) -> wait n seconds to establish a connection, then wait m seconds to get a response
try:
    response = requests.get('https://api.github.com', timeout=1.5)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

# Response status code
# We can check status_code or use  raise_for_status to raise an exception if the request was unsuccessful
try:
    print(response.status_code)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
else:
    print('Success!')

# Get response content
# content  -> return response content in bytes
# hearders -> return response headers
# encoding -> provide an explicit encoding
# text     -> convert content into string (encoding is based on headers)
# json()   -> return response data as a dictionary
response.encoding = 'utf-8'
print(response.content)
print(response.text)
print(response.headers["Content-Type"])
data = response.json()

# Query parameters in a request
# To query parameters, we add key-value pairs to 'params' parameter
# To customize headers, you pass a dictionary of HTTP headers
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}
)

# Inspect some attributes of the 'requests' repository
# We can access data same as with any dictionary in Python
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')
print(f'Text matches: {repository["text_matches"]}')






# -----------------POST REQUEST-----------------

# Send data from a specified resource with post()
# Data takes a dictionary, a list of tuples, bytes, or a file-like object
requests.post('https://httpbin.org/post', data={'key': 'value'})

# Send json data with 'json' parameter
response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.url)

# Inspect data before sending a post request
print(response.request.headers['Content-Type'])
print(response.request.url)
print(response.request.body)
