#/usr/bin/python3
import requests

### import antigravity

### HANDLING BINARY DATA 
req = requests.get('https://imgs.xkcd.com/comics/nerd_sniping.png')
# print( req.ok )
with open('../testfiles_output/comic.png','wb') as f:
    f.write(req.content)

### USING PARAMETERS
req = requests.get( 'https://httpbin.org/get?page=4&count=239' )
print(req.text)
req = requests.get( 'https://httpbin.org/get', params = { "page": 4, "count": 239 } )
print(req.text)

req = requests.post( 'https://httpbin.org/post', data = { "page": 4, "count": 239 } )
print(req.text)

req_dict = req.json()
print(req_dict['form']['page'])

#### AUTH
user = 'TESTUSER'
passwd = 'TESTING'
req = requests.get( f'https://httpbin.org/basic-auth/{user}/{passwd}', auth = (user,passwd)  )
# print(req.text)
print(req.status_code)

req = requests.get( f'https://httpbin.org/basic-auth/{user}/{passwd}FALSE', auth = (user,passwd), timeout = 3  )
print(req.status_code)


try: 
    req = requests.get( f'https://httpbin.org/delay/6', timeout = 3  )
except Exception as E: 
    print( E )