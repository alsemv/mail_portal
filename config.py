import urllib


class BaseConfig(object):
  DEBUG = False


class Dev(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus('DRIVER={ODBC Driver 11 for SQL Server};SERVER=DFM15\SQLEXPRESS;DATABASE=cantine;UID=sa;PWD=dfm_2017!;'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Flask-User
    USER_APP_NAME = "Cantine Riunite"
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_REQUIRE_RETYPE_PASSWORD = False

    SERVER_NAME = '127.0.0.1:4995'

class Prod(BaseConfig):
    pass