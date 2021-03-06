import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def create_first_keyboard(text, color_key):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(text, color=color_key)
    return keyboard


def create_yes_or_no(text_yes, no_text):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(text_yes, color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button(no_text, color=VkKeyboardColor.NEGATIVE)
    return keyboard


def create_menu():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Факты', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Викторина', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Еще что-то', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Еще что-то', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Еще что-то', color=VkKeyboardColor.PRIMARY)
    return keyboard


def generate_answers_button(answers: list):
    keyboard = VkKeyboard(one_time=True)
    true_answer = answers[0]
    false_answers = answers[1:]
    r = random.randint(0, len(answers))
    h = 0
    for i in range(0, len(answers), 2):
        if i == r:
            keyboard.add_button(true_answer, color=VkKeyboardColor.PRIMARY)
            keyboard.add_button(false_answers[h], color=VkKeyboardColor.PRIMARY)
            h += 1
        else:
            if i+1 == r:
                keyboard.add_button(false_answers[h], color=VkKeyboardColor.PRIMARY)
                keyboard.add_button(true_answer, color=VkKeyboardColor.PRIMARY)
                h += 1
            else:
                keyboard.add_button(false_answers[h], color=VkKeyboardColor.PRIMARY)
                keyboard.add_button(false_answers[h+1], color=VkKeyboardColor.PRIMARY)
                h += 2
        keyboard.add_line()
    keyboard.add_button('Отбой', color=VkKeyboardColor.NEGATIVE)
    return keyboard, true_answer


