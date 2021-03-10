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
        del list_line[0]
        del list_line[-1]
        h = 0
        for j in list_line:
            result.append(j[4:-5])
    r = rand.randint(0, len(result))
    return result[r]


def give_space():
    constellations_list = [
        {
            'name': 'Малая медведица',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Большая медведица',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Геркулес',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Пегас',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Кассиопея',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Гидра',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Дева',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Центавр',
            'url': 'images/small_beer.jpg'
        },
        {
            'name': 'Цефей',
            'url': 'images/sozvezdie-cefei.jpg'
        },
        {
            'name': 'Дракон',
            'url': 'images/sozvezdie-cefei.jpg'
        }
    ]
    r = rand.randint(0, len(constellations_list) - 1)
    return constellations_list[r]
