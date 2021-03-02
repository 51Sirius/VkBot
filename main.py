import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import cfg
from vk_bot import VkBot


vk_session = vk_api.VkApi(token=cfg.TOKEN)
long_poll = VkLongPoll(vk_session)


for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text
            bot = VkBot(event.user_id, message, vk_session)
            bot.command()
