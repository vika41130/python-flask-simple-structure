import os

MESSAGE = {
    'SERVER_ERROR': 'SERVER_ERROR'
}

UPLOAD = {
    'FOLDER': 'static\\uploaded'
}

def get_path():
    parent_path = os.path.dirname(os.path.realpath(__file__))
    # return os.path.join(parent_path, UPLOAD.get('FOLDER'))
    return parent_path