import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from functionsAndClass.vk_bot import VkBot
import os
import sqlite3
import logging
import cfg
import time
import requests


try:
    vk_session = vk_api.VkApi(token=cfg.TOKEN)
    long_poll = VkLongPoll(vk_session)
    users_quest = {1: []
                   }
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    logging.basicConfig(level=logging.INFO, filename=u'logs.log')

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                try:
                    message = event.text
                except Exception as exc:
                    logging.error(exc)
                    message = 'Меню'
                try:
                    cursor.execute("SELECT vk_id FROM users WHERE vk_id=?", (event.user_id,))
                    if cursor.fetchone() is None:
                        cursor.execute("INSERT INTO users(vk_id) VALUES (?)", (event.user_id,))
                        conn.commit()
                    cursor.execute("SELECT quest_amount FROM users WHERE vk_id=?", (event.user_id,))
                    point = cursor.fetchone()[0]
                except Exception as exc:
                    logging.error(exc)
                    point = 0
                try:
                    bot = VkBot(event.user_id, message, vk_session, point)
                    logging.info(f'Created bot for {event.user_id}')
                    if users_quest.get(event.user_id) is not None:
                        answer = users_quest.get(event.user_id)[0]
                        cont = bot.answer_session(answer)
                        users_quest.pop(event.user_id)
                        cursor.execute("SELECT quest_amount FROM users WHERE vk_id=?", (event.user_id,))
                        amount = cursor.fetchone()[0]
                        cursor.execute(f"UPDATE users SET quest_amount={amount+1} WHERE vk_id={event.user_id}")
                        conn.commit()
                    else:
                        go = bot.command()
                        if go:
                            users_quest[event.user_id] = [bot.answer, bot.wrong_answers]
                except Exception as exc:
                    logging.error(exc)
except requests.exceptions.ReadTimeout:
    print("\n Переподключение к серверам ВК \n")
    time.sleep(3)
