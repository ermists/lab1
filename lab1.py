import requests
import re

def more(text):
    count=0
    for line in text.plit('\n'):
        print(line)
        count+=1
        if count % 30 ==0:
            reply=input('show more (y/n)? ')
            if reply == 'n':
                break

url = input ('Enter a url: ')

if not url.startswith('http://'):
    url = 'http://' + url

print(url)
with requests.get(url) as response:

    print(f"Website headers are {url} \n, {response.headers} \n\n")


    server=response.headers.get('Server')
    if server:
        print (f"The server is {server}")
    else:
        print("no server found")

    
    cookies = response.headers.get('Set-Cookie')
    if cookies:
        cookies=re.split('SameSite=[a-z]+, ',cookies)
        for cookie in cookies:
            cookie=cookie.split(';')
            print(f"This cookie's name is {cookie[0]}")
        
    else:
        print('No cookie found')

