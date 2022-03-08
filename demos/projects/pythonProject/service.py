from collections import namedtuple
from xml.etree.ElementTree import ElementTree

import requests

Episode = namedtuple('Episode', 'title, link, date, id')
episodes = {}


def download_info():
    url = 'https://talkpython.fm/episodes/rss'
    
    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    print(len(items))
