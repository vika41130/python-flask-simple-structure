from flask import Flask

from members.members import members_bp
from file.upload import upload_bp
from file.send_file import send_file_bp

from mysql import mysql

app = Flask(__name__)
app.register_blueprint(members_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(send_file_bp)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'msql1121AM@ttc'
app.config['MYSQL_DATABASE_DB'] = 'myflixdb'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'


# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


mysql.init_app(app)



# def create_app(config_file='app.config.py'):
# app.config.from_pyfile(config_file)
# return app

