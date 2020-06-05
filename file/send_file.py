from flask import send_from_directory, Blueprint, send_file, abort
from constant import UPLOAD, get_path
import os

send_file_bp = Blueprint('send_file_bp',__name__)

@send_file_bp.route('/media/<file_name>', methods=['GET'])
def send_media(file_name):
    print('file_name',file_name)
    try:
        root = get_path()
        print('root',root)
        path = os.path.join(root, 'static','uploaded')
        print(path)
        return send_from_directory(path, filename=file_name, as_attachment=True)
        # return 'ok'
    except FileNotFoundError:
        abort(404)
        print('error')
        # return 'error'


@send_file_bp.route('/mediaa/<string:name>', methods=['GET'])
def test(name):
    return name
