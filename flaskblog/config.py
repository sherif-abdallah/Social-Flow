import os


class Config:
    SECRET_KEY = "4f4e245bdd015a66f8f267b91fcb75ff"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'example@domain.com'
    MAIL_PASSWORD = 'password'
