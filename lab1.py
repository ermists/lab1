import requests
import re

url = input ('Enter a url: ')

if not url.startswith('http://'):
    url = 'http://' + url

with requests.get(url) as response:

    print(f"Website headers are {url} \n, {response.headers} \n\n")


    server=response.headers.get('Server')
    if server:
        print (f"The server is {server}")
    else:
        print("no server found")

    
    cookies = response.cookies
    if cookies:
       for cookie in cookies:
            print(f"This cookie's name is {cookie.name}")
    else:
        print('No cookie found')

