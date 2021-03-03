import bs4
import requests


def parsing_facts():
    req = requests.get('http://interesnyjfakt.ru/top-100-interesnyx-faktov-o-kosmose/')
    bs: str = bs4.BeautifulSoup(req.text, "html.parser")
    result = ""
    for i in list(bs):
        pass
