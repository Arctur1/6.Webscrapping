import requests
from bs4 import BeautifulSoup, Tag

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('response is not valid')

soup = BeautifulSoup(response.text, features="html.parser")

for article in soup.find_all('article'):
    hubs = {h.text for h in article.find_all('div', class_='post__text_v2')}
    for hub in hubs:
        for keyword in KEYWORDS:
            if keyword in hub:
                title: Tag = article.find('h2', class_='post__title')
                a: Tag = title.find('a')
                href = a.attrs.get('href')
                time = article.find('span', class_='post__time')
                print(f'{time.text.capitalize()}{title.text}{href}')
