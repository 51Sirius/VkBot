# [КосмоБот](https://vk.com/public202952694)
Бот вконтакте на всероссийский конкурс проводимый Московским районом города Санкт-Петербурга. Ко дню празднования 60-летия полёта первого человека в космос.

## Основные возможности

- [x] Викторина;
- [x] Факты о космосе;
- [x] База данных с пользователями;
- [x] Выдача премиальной аватарки;

## Будущие дополнения

- [ ] Записи на стене прошедшим викторину;
- [ ] Добавление новых вопросов и созвездий;
- [ ] Рейтинг участников;

## Используемые библиотеки

- vk_api
- requests
- bs4
- Pillow
- sqlite3

## Факты
факты парсятся с сайта с помошью библиотек requests и bs4.
[Сайт](http://interesnyjfakt.ru/top-100-interesnyx-faktov-o-kosmose/)

## Построение аватарки
Сначала парсится изображение пользователя со страницы вк, после скачивается. Потом идет обработка очков пользователя и добавляется на фон. Далле изображение пользователя накладывается на фон с очками и рангом.
