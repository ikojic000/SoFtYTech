# MAIN PYTHON FILE IN A flaskblog PACKAGE

# Imports

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_mail import Mail
import flask_whooshalchemy as wa
import flaskfilemanager


# App Configuration
app = Flask(__name__)
db = SQLAlchemy(app)
mail = Mail()
mail.init_app(app)

from flaskblog.config import Config

app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = "users.login"

from flaskblog.models import User, Post

# from flask_user import UserManager
from flaskblog.customUserManager import CustomUserManager


from flaskblog.users.utils import accessControl_function

flaskfilemanager.init(app, access_control_function=accessControl_function)

wa.whoosh_index(app, Post)


# Routes are last to be imported

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.comments.routes import comments
from flaskblog.main.routes import main
from flaskblog.logs.routes import logs
from flaskblog.errors.routes import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(comments)
app.register_blueprint(main)
app.register_blueprint(logs)
app.register_blueprint(errors)


user_manager = CustomUserManager(app, db, User)
