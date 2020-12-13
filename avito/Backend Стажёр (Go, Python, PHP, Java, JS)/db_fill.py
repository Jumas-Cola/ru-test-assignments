import requests
import json
import random


url = 'http://127.0.0.1:8000/announcements/'

for _ in range(50):
    price = random.random() * 1000
    payload = {
        'name': 'string',
        'price': price,
        'description': 'string',
        'photos': [
            'https://docs.python.org/3/_static/py.png',
            'https://tinyjpg.com/images/social/website.jpg',
            'https://media.emailonacid.com/wp-content/uploads/2019/03/2019-GifsInEmail.gif'
        ]
    }
    requests.post(url, json=payload)
