import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import cfg
import random as rand

vk_session = vk_api.VkApi(token=cfg.TOKEN)
long_poll = VkLongPoll(vk_session)


def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    try:
        vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
    except Exception as exc:
        print(exc)


for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "Hi":
                write_msg(event.user_id, "Hi")
            elif request == "bye":
                write_msg(event.user_id, "bye((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
