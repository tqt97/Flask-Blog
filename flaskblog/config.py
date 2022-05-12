# import os

class Config:
    SECRET_KEY = '58fed6d2d4e1eae1c6e0ad8bf0a80d57'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kutuanonline199@gmail.com'
    MAIL_PASSWORD = 'Tuquoc2021'
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
