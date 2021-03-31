from PIL import Image, ImageDraw, ImageFont
import requests
import os


def prepare_mask(size, antialias=2):
    mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    return mask.resize(size, Image.ANTIALIAS)


def crop(im, s):
    w, h = im.size
    k = w / s[0] - h / s[1]
    if k > 0:
        im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0:
        im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
    return im.resize(s, Image.ANTIALIAS)


def write_text(amount_answers, image_url, rank, user_id):
    try:
        image = Image.open(image_url)
        draw = ImageDraw.Draw(image)
        text_answers = f"Кол-во ответов: {amount_answers}"
        text_rank = f"Звание: {rank}"
        font = ImageFont.truetype("arial.ttf", size=30)
        draw.text((440, 100), text_answers, font=font)
        draw.text((440, 200), text_rank, font=font)
        image.save(f"users-image\\bg{user_id}.jpg")
    except Exception as e:
        print(f"[ERROR] {e}")


def paste_image(first, second, id_user):
    im1 = Image.open(first)
    im2 = Image.open(second)
    im1.paste(im2, (90, 50))
    im1.save(f'users-image\\user{id_user}.jpg', quality=75)
    im1.close()
    im2.close()
    os.remove(f'users-image\\avatar{id_user}.jpg')
    os.remove(f'users-image\\bg{id_user}.jpg')


def save_image(url, id_user):
    resp = requests.get(url, stream=True).raw
    img = Image.open(resp)
    img.save(f'users-image\\avatar{id_user}.png', 'png')
    img = Image.open(f'users-image\\avatar{id_user}.png')
    img = img.resize((300, 300), Image.ANTIALIAS)
    img.save(f'users-image\\avatar{id_user}.jpg', 'jpeg')
    os.remove(f'users-image\\avatar{id_user}.png')
