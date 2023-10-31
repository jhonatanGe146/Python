import requests
url= 'http://httpbin.org/cookies'

#sesion= r.session()
mycookies= {
    'usuario': 'Jhonatan Gelvis',
    'Contrasena': 'jhonas'
    }

response=requests.get(url, cookies=mycookies)
print(response.content.decode())
print('='*80)
print(response.cookies)