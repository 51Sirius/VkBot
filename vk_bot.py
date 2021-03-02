import bs4
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class VkBot:
    def __init__(self, user_id, message, session):
        self.session = session
        self.message = message
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id()
        self._COMMANDS = ["", "", ""]
        print(f'Create bot for {self._USERNAME}')

    def _get_user_name_from_vk_id(self):
        req = requests.get("https://vk.com/id" + str(self._USER_ID))
        bs = bs4.BeautifulSoup(req.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        return result

    def command(self):
        pass

    def write_msg(self, message):
        random_id = vk_api.utils.get_random_id()
        try:
            self.session.method('messages.send', {'user_id': self._USER_ID, 'message': message, "random_id": random_id})
        except Exception as exc:
            print(exc)