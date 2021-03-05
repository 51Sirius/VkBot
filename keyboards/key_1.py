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
