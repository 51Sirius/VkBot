import bs4
import requests
import vk_api
from functionsAndClass.key_1 import *
from functionsAndClass import parser_space
from functionsAndClass.questions import give_question
from functionsAndClass.images import *


class VkBot:
    def __init__(self, user_id, message: str, session, point, first):
        self.first = first
        self.Upload = vk_api.VkUpload(session)
        self.answer = None
        self.wrong_answers = []
        self.session = session
        self.message = message
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id()
        self._COMMANDS = ["Привет!", "Да, хочу", 'Ещё!', "Не, я и так крут!", "Нет, спасибо", 'Факты', 'Викторина',
                          'Хватит', 'Меню', 'Созвездия', 'Профиль']
        print(f'Create bot for {self._USERNAME} / {self._USER_ID}')
        self.points = point

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
            self.write_msg('Привет! Рад тебя видеть. Хочешь немного фактов о космосе?',
                           create_yes_or_no(self._COMMANDS[1], self._COMMANDS[3]))
        elif self.message == self._COMMANDS[1] or self.message == self._COMMANDS[5] or self.message == 'Да':
            self.write_msg('Подождите секундочку...')
            try:
                self.write_msg(parser_space.parsing_facts())
                self.write_msg('\nЕще фактов?', create_yes_or_no(self._COMMANDS[1], self._COMMANDS[4]))
            except:
                self.write_msg('Произошла ошибка, попробуйте еще раз.',
                               create_yes_or_no(self._COMMANDS[1], self._COMMANDS[4]))
        elif self.message == self._COMMANDS[6] or self.message == self._COMMANDS[2]:
            quest, answers = give_question()
            keyboard, true_answer = generate_answers_button(answers)
            self.write_msg(quest, keyboard)
            self.answer = true_answer
            self.wrong_answers = answers[1:]
            return True
        elif self.message == self._COMMANDS[4] or self._COMMANDS[3] == self.message or self._COMMANDS[7] == \
                self.message or self.message == self._COMMANDS[8]:
            self.write_msg('Тогда вот вам навигационное меню.', create_menu())
        elif self._COMMANDS[9] == self.message or self.message == 'Еще созвездий':
            constellation = parser_space.give_space()
            self.write_msg(constellation['name'], create_yes_or_no('Еще созвездий', self._COMMANDS[7]),
                           constellation['url'])
        elif self.message == 'Еще что-то':
            self.write_msg('Это тестовое поле его лучше пока не трогать)', create_menu())
        elif self.message == self._COMMANDS[10]:
            avatar_url, hide = parser_space.parsing_avatar(self._USER_ID)
            save_image(avatar_url, self._USER_ID)
            if self.points < 20:
                rank = 'Новичок'
            elif 20 <= self.points < 100:
                rank = 'Звездочет'
            elif self.points >= 100:
                rank = 'Космонавт'
            else:
                rank = 'Призыватель душ'
            write_text(self.points, "users-image/bg.jpg", rank, self._USER_ID)
            paste_image(f"users-image/bg{self._USER_ID}.jpg", f'users-image/avatar{self._USER_ID}.jpg', self._USER_ID)
            if hide:
                ms = 'К сожалению, у Вас закрытый профиль, поэтому мы не смогли получить фотографию 😢'
            else:
                ms = None
            self.write_msg(f'Ваш ранк: {rank} \nКоличество верных ответов: {self.points}\n' + ms, create_menu(),
                           f'users-image/user{self._USER_ID}.jpg')
        elif self.message == 'Инструкция':
            self.write_msg(
                'Список команд:\n1.Факты о космосе - Факты\n2.Викторина - Викторина\n3.Случайное созвездие - Созвездия\
                \n4.Специальная аватарка - Профиль\nРекомендуем для корректной работы бота использовать кнопки\
                 Вконтакте. На некоторых устройствах для их активации необходимо нажать на квадрат рядом с полем ввода\
                текста.',
                create_menu())
        else:
            self.write_msg(
                'Команда была некорректной.\n Если вы хотите получить список команд, то напишите "Инструкция"',
                create_menu())
        return False

    def write_msg(self, message, keyboard=None, image=None):
        random_id = vk_api.utils.get_random_id()
        try:
            if keyboard is not None:
                if image is not None:
                    attachments = []
                    photo_upload = self.Upload.photo_messages(photos=image)[0]
                    attachments.append('photo{}_{}'.format(photo_upload['owner_id'], photo_upload['id']))
                    self.session.method('messages.send',
                                        {'user_id': self._USER_ID, 'message': message, "random_id": random_id,
                                         'keyboard': keyboard.get_keyboard(), 'attachment': ','.join(attachments)})
                else:
                    self.session.method('messages.send',
                                        {'user_id': self._USER_ID, 'message': message, "random_id": random_id,
                                         'keyboard': keyboard.get_keyboard()})
            else:
                self.session.method('messages.send',
                                    {'user_id': self._USER_ID, 'message': message, "random_id": random_id})
        except Exception as exc:
            print(exc)

    def answer_session(self, answer):
        if self.message == answer:
            self.write_msg('Молодец, это был правильный ответ!!!', create_yes_or_no('Ещё!', 'Хватит'))
            return True
        else:
            if self.message == 'Отбой':
                self.message = self._COMMANDS[8]
                self.command()
            else:
                self.write_msg('Ну почти', create_yes_or_no('Ещё!', 'Хватит'))
            return False
