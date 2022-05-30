import os
import secrets
from PIL import Image
from flask import current_app



def save_picture(image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/images/posts', picture_fn)
    output_size = (400, 300)
    i = Image.open(image)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
