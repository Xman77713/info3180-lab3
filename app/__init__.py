from flask import Flask
from flask_mail import Mail
from .config import Config
from app import views

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)