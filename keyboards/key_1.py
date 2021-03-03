from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def create_first_keyboard(text, color_key):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(text, color=color_key)
    return keyboard
