from pathlib import Path
import base64
import logging

def img_to_bytes(img_path):
    try:
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded
    except Exception as ex:
        logging.error(f'Error in img_to_bytes: {ex}')
        return None

def img_to_html(img_path, img_format, css_id):
    try:
        img_html = f"<img src='data:image/{img_format}+xml;base64,{img_to_bytes(img_path)}' class='img-fluid' id='{css_id}'>"
        return img_html
    except Exception as ex:
        logging.error(f'Error in img_to_html: {ex}')
        return None