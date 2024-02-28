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
            cookie[0]=cookie[0].split('=')
            print(f"This cookie's name is {cookie[0][0]}")
            if 'Expires' or 'expires' in cookie[2]:
                cookie[2]=cookie[2].split('=')
                print(f"This cookie expires at {cookie[2][1]}")
            elif 'Expires' or 'expires' in cookie[1]: 
                cookie[1]=cookie[1].split('=')
                print(f"This cookie expires at {cookie[1][1]}")
            elif 'Expires' or 'expires' in cookie[3]: 
                cookie[3]=cookie[3].split('=')
                print(f"This cookie expires at {cookie[3][1]}")
            else : print('This cookie does not have an expiry date')
            
        
    else:
        print('No cookie found')

