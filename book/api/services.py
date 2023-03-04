import requests
import json


def get_book(search):
    url = 'https://www.googleapis.com/books/v1/volumes?q='
    url += search
    params = {'search': search}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data
