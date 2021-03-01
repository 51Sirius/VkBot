import vk_api
import cfg


vk_session = vk_api.VkApi(cfg.TOKEN, cfg.PASSWORD)
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))