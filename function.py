import json
import time

import pymongo
import requests

mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
dbf = mongo['bilibili']['UP02']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}


def random_proxies():
    response = json.loads(requests.get('http://127.0.0.1:5000/proxies/http').text)
    return random.choice(response['proxies'])


def get_response(url: str, is_proxy=True):
    response = ''
    if is_proxy is True:
        response = requests.get(url, headers=headers, proxies={'https': random_proxies()})
    elif is_proxy is False:
        response = requests.get(url, headers=headers)
    return response
