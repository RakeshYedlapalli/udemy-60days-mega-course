import requests
from send_email_via_web import sendemailViaWeb


url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-03-17&sortBy="
       "publishedAt&apiKey=287ca0b41cb748dca8a8c23e50bbf3b4")


api_key = "287ca0b41cb748dca8a8c23e50bbf3b4"


request = requests.get(url)
content = request.json()

i = 0
# for article in content['articles']:
       # print(article['title'])
       # print(article['description'])

title = content['articles']
print(title[0]['title'])
print(title[0]['description'])


sendemailViaWeb('rak.mdg94@gmail.com',f"{title[0]['title']}-{title[0]['description']}")

