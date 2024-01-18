"""
REQUEST:
-Standard library to make HTTP request
-Response content will be a serialized JSON content
-Exceptions:
    -In the event of a network problem (e.g. DNS failure, refused connection, etc.), Requests will
    raise a ConnectionError exception.
    -In the event of the rare invalid HTTP response, Requests will raise an HTTPError exception.
    -If a request times out, a Timeout exception is raised.
    -If a request exceeds the configured number of maximum redirections, a TooManyRedirects
    exception is raised.
    -All exceptions that Requests explicitly raises inherit from
    requests.exceptions.RequestException.
"""

import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout


# -----------------GET REQUEST-----------------

# Retrieve data from a specified resource with get()
response = requests.get('https://api.github.com')

# Timeout your request
# timeout=n      -> wait n secsbefore timeout
# timeout=(n, m) -> wait n secs to establish a connection, then wait m secs to get a response
try:
    response = requests.get('https://api.github.com', timeout=1.5)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

# Response status code
# We can check status_code or use  raise_for_status to raise an exception if the request was
# unsuccessful
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
