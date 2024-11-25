from werkzeug.utils import secure_filename
import os
from flask import current_app

def save_avatar(form_avatar):
    filename = secure_filename(form_avatar.filename)
    filepath = os.path.join(current_app.root_path, 'static/images', filename)
    form_avatar.save(filepath)
    return filename
