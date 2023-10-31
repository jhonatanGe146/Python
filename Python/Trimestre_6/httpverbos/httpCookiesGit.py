import requests
url= 'https://api.github.com/users'

sesion= requests.session()
sesion.auth=('jhonatangelvis@gmail.com', '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')
response=sesion.get(url)

print(response.status_code)

if response.ok:
    response1=sesion.get('https://github.com/jhonatanGe146')
    print(response1.cookies)
    