import random as rand

quest_list = {
    0: ['Какая страна первой запустила спутник?', ['СССР', 'Америка', 'Атлантида', 'Япония']],
    1: ['Кто является первой женщиной-космонавтом?', ['Валентина Терешкова', 'Светлана Савицкая', 'Елена Кондакова',
                                                      'Елена Серова']],
    2: ['Как назывался корабль, на котором 12 апреля 1961 года Юрий Гагарин совершил первый полёт в космос?',
        ['Восток', '']],
    3: ['Какой ученый является изобретателем космической ракеты?', 'Циолковский'],
    4: ['Что в переводе с греческого означает "комета"?', 'Хвостатая звезда'],
    5: ['Какие планеты солнечной системы вращаются в направлении, противоположном Земле?', 'Венера и Уран'],
    6: ['На какой максимальной высоте находился корабль во время полета Гагарина?', '302 километра'],
    7: ['Что является причиной образования кратеров на Луне?', 'метеориты'],
    8: ['Кто стал первым "космическим туристом"?', 'Деннис Тито'],
    9: ['Как звали человека, который первым высадился на Луну?', 'Нил Армстронг'],
    10: ['Какой астронавт был вторым (вслед за Леоновым) вышедшим в открытый космос?', 'Эдвард Уайт'],
    11: ['Как называется ближайшая к Солнцу планета?', 'Меркурий']
}


def give_question():
    r = rand.randint(0, 2)
