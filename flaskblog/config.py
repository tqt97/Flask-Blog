# import os

class Config:
    SECRET_KEY = '58fed6d2d4e1eae1c6e0ad8bf0a80d57'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://lznppakuwhysao:61661e0cbb69f27c878bef0025cdc839d9557719f30ad996608b072c00382e08@ec2-52-200-215-149.compute-1.amazonaws.com:5432/d4gmmoe235cob2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kutuanonline199@gmail.com'
    MAIL_PASSWORD = 'Tuquoc2021'
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
