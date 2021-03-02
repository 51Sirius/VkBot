import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import cfg
from vk_bot import VkBot


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
            message = event.text
            bot = VkBot(event.user_id, message)
