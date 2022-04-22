from flask import Flask
from flask_cors import CORS

from api.user import user


app = Flask(__name__)
CORS(app)
app.register_blueprint(user)
