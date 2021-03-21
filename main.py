import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from functionsAndClass.vk_bot import VkBot
import os
import sqlite3

vk_session = vk_api.VkApi(token=os.environ['TOKEN'])
long_poll = VkLongPoll(vk_session)
users_quest = {1: []
               }
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text
            last = message
            try:
                bot = VkBot(event.user_id, message, vk_session)
            except:
                print('Error create bot')
            try:
                if users_quest.get(event.user_id) is not None:
                    answer = users_quest.get(event.user_id)[0]
                    bot.answer_session(answer)
                    users_quest.pop(event.user_id)
                else:
                    go = bot.command()
                    if go:
                        users_quest[event.user_id] = [bot.answer, bot.wrong_answers]
            except Exception as exc:
                print(exc)
