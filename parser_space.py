import bs4
import requests
import random as rand


def parsing_facts():
    req = requests.get('http://interesnyjfakt.ru/top-100-interesnyx-faktov-o-kosmose/')
    bs: bs4.BeautifulSoup = bs4.BeautifulSoup(req.text, "html.parser")
    bs = bs.findAll('ul')[1:18]
    result = []
    for i in list(bs):
        pass


