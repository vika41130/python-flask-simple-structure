from flask import Blueprint, request, redirect, jsonify, make_response
import os
from datetime import datetime
from constant import UPLOAD

if not os.path.exists(UPLOAD.get('FOLDER')):
    os.mkdir(UPLOAD.get('FOLDER'))

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print('file',file)
    print('file.mimetype', file.mimetype)
    print(file.filename)
    path = os.path.join(UPLOAD.get('FOLDER'))
    print('path',path)
    # file.save(os.path.join(UPLOAD.get('FOLDER'), str(datetime.now().microsecond)) + extension(file.mimetype))
    file.save(os.path.join(UPLOAD.get('FOLDER'), file.filename))
    _obj = {
        'result': {
            'status': 'Ok',
            'url': 'url_file_uploaded',
        }
    }
    resp = make_response(jsonify(_obj), 200)
    return resp

def extension(mimetype):
    if mimetype == 'video/mp4':
        return '.mp4'
    if mimetype == 'image/png':
        return '.png'
    if mimetype == 'image/jpg':
        return '.jpg'
    if mimetype == 'image/jpeg':
        return '.jpg'
    return '.any'
