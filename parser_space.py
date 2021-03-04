import bs4
import requests
import random as rand


def parsing_facts():
    req = requests.get('http://interesnyjfakt.ru/top-100-interesnyx-faktov-o-kosmose/')
    bs: bs4.BeautifulSoup = bs4.BeautifulSoup(req.text, "html.parser")
    bs = bs.findAll('ul')[1:18]
    result = []
    for i in list(bs):
        i = str(i)
        list_line = i.split('\n')
        h = 0
        for j in list_line:
            result.append(i.split('\n'))


parsing_facts()
