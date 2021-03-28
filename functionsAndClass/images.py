from PIL import Image, ImageDraw, ImageFont


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


def circle_crop(size=(100, 100), image_url='..\images\avatar.png'):
    im = Image.open(image_url)
    im = crop(im, size)
    im.putalpha(prepare_mask(size, 4))
    im.save(image_url)


def write_text(amount_answers, image_url, rank, user_id):
    try:
        image = Image.open(image_url)
        draw = ImageDraw.Draw(image)
        text_answers = f"Количество верных ответов: {amount_answers}"
        text_rank = f"Ваше звание: {rank}"
        font = ImageFont.truetype("arial.ttf", size=18)
        draw.text((140, 30), text_answers, font=font)
        draw.text((140, 60), text_rank, font=font)
        image.save(f"../images/bg{user_id}.jpg")
    except Exception as e:
        print(f"[ERROR] {e}")


def paste_image(first, second, id_user):
    im1 = Image.open(first)
    im2 = Image.open(second)
    im1.paste(im2, (20, 50))
    im1.save(f'user{id_user}.png', quality=95)
    im1.close()
    im2.close()
