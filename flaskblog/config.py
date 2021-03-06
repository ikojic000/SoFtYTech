from flaskblog import app
import os


filemanager_route = os.path.join(app.root_path, 'static/upload')


class Config:
    SECRET_KEY = 'y.o.u.s.h.a.l.l.n.o.t.k.n.o.w'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:administrator@localhost/softy?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    USER_EMAIL_SENDER_EMAIL = 'softythetechguy@gmail.com'
    USER_APP_NAME = 'SoftyTech'
    USER_LOGIN_TEMPLATE = '/admin_Login.html'
    USER_FORGOT_PASSWORD_TEMPLATE = '/resetPassword.html'
    USER_CHANGE_PASSWORD_TEMPLATE = '/changePassword.html'
    USER_LOGIN_URL = '/login'
    USER_CHANGE_PASSWORD_URL = '/user/change-password'
    USER_ENABLE_USERNAME = False
    USER_AUTO_LOGIN_AFTER_RESET_PASSWORD = False
    FLASKFILEMANAGER_FILE_PATH = filemanager_route

# ALTER TABLE comment CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE comment modify name text charset utf8mb4;

# 'mysql://root:administrator@localhost/softy'
# 'mysql+pymysql://root:administrator@localhost/softy?charset=utf8mb4'
# 'sqlite:///site.db'