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
            'url': 'https://avatars.mds.yandex.net/get-turbo/4281005/rth2f02bfc4ec6ac47d5cd6aea3d93b6263/max_g480_c12_r1x1_pd10'
        },
        {
            'name': 'Большая медведица',
            'url': 'https://avatars.mds.yandex.net/get-turbo/4080869/rth1fe82b80ba8be0b6cafaab85f409a226/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Геркулес',
            'url': 'https://avatars.mds.yandex.net/get-turbo/4292885/rth44e84e960765243a2bb95719c462e1d7/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Пегас',
            'url': 'https://avatars.mds.yandex.net/get-turbo/3039741/rth5394ed803b8e91a60f6286825dcd3a0e/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Кассиопея',
            'url': 'https://avatars.mds.yandex.net/get-turbo/2350003/rth77b8266d9b615262bc01ecb2ac3eb0d8/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Гидра',
            'url': 'https://avatars.mds.yandex.net/get-turbo/4080869/rthb7a2a944df245f694d2c335ad22bcf07/max_g480_c12_r16x9_pd10'
        },
        {
            'name': 'Дева',
            'url': 'https://avatars.mds.yandex.net/get-turbo/3506797/rth27680f5aad290c52c7f0fc3ee3aea3bc/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Центавр',
            'url': 'https://avatars.mds.yandex.net/get-turbo/2910686/rth7a9c9ba1baa8a8fa296b97c41003288b/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Цефей',
            'url': 'https://avatars.mds.yandex.net/get-turbo/4446033/rth3bc016f46199cc8442e2522b5770b40b/max_g480_c12_r4x3_pd10'
        },
        {
            'name': 'Дракон',
            'url': 'https://avatars.mds.yandex.net/get-turbo/1676318/rth53d3a3011d78e845ed12598efdf0097d/max_g480_c12_r4x3_pd10'
        }
    ]
    r = rand.randint(0, len(constellations_list)-1)
    return constellations_list[r]