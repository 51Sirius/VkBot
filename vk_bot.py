import bs4
import requests
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from keyboards.key_1 import *
import parser_space


class VkBot:
    def __init__(self, user_id, message, session):
        self.session = session
        self.message = message
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id()
        self._COMMANDS = ["Привет!", "Да, хочу", 'Ещё!', "Не, я и так крут!", "Нет, спасибо"]
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
        if self.message == self._COMMANDS[0] or self.message == 'привет' or self.message == 'Привет':
            self.write_msg('Привет рад тебя видеть. Не хочешь немного фактов о космосе?',
                           create_yes_or_no(self._COMMANDS[1],self._COMMANDS[3]))
        elif self.message == self._COMMANDS[1]:
            self.write_msg('Подождите секундочку...')
            self.write_msg(parser_space.parsing_facts())
            self.write_msg('\nЕще фактов?',create_yes_or_no(self._COMMANDS[1], self._COMMANDS[4]))
        elif self.message == self._COMMANDS[2]:
            pass
        elif self.message == self._COMMANDS[3]:
            pass

    def write_msg(self, message, keyboard=None):
        random_id = vk_api.utils.get_random_id()
        try:
            if keyboard is not None:
                self.session.method('messages.send',
                                    {'user_id': self._USER_ID, 'message': message, "random_id": random_id,
                                     'keyboard': keyboard.get_keyboard()})
            else:
                self.session.method('messages.send',
                                    {'user_id': self._USER_ID, 'message': message, "random_id": random_id})
        except Exception as exc:
            print(exc)
