import requests

url= 'https://previews.123rf.com/images/ewastudio/ewastudio2303/ewastudio230300647/199595690-dos-dragones-que-escupen-fuego-dragones-peleando-ai-generativa.jpg'
response=requests.get(url, stream=True)
with open ('Python\Trimestre_6\httpverbos\drangon.jpg', 'wb') as  pythonimg:
    for i in response.iter_content():
        pythonimg.write(i)