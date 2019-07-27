import os

class Config():
  SECRET_KEY = os.environ.get('SECRET_KEY') #'b680f9c461dca3d215fca7e59a4838b1'

  """ DATABASE SETUP """
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

  """email setup for gmail"""
  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = os.environ.get('EMAIL_ACCOUNT')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True