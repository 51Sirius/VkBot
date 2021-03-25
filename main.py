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
            cursor.execute("SELECT vk_id INTO users WHERE vk_id=?", event.user_id)
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO uesers(vk_id) VALUES ?", event.user_id)
                conn.commit()
            try:
                bot = VkBot(event.user_id, message, vk_session)
            except:
                print('Error create bot')
            try:
                if users_quest.get(event.user_id) is not None:
                    answer = users_quest.get(event.user_id)[0]
                    cont = bot.answer_session(answer)
                    users_quest.pop(event.user_id)
                    cursor.execute("SELECT quest_amount INTO users WHERE vk_id=?", event.user_id)
                    amount = cursor.fetchone()
                    cursor.execute("UPDATE users SET amount=? WHERE vk_id=?", (amount+1, event.user_id))
                else:
                    go = bot.command()
                    if go:
                        users_quest[event.user_id] = [bot.answer, bot.wrong_answers]
            except Exception as exc:
                print(exc)
