import pyodbc


class Database(object):

    server = 'DFM15\SQLEXPRESS'
    database = 'cantine'
    username = 'sa'
    password = 'dfm_2017!'

    @staticmethod
    def getcursor():
        connect = pyodbc.connect(
            'DRIVER={ODBC Driver 11 for SQL Server};SERVER=' + Database.server + ';DATABASE=' + Database.database + ';UID=' + Database.username + ';PWD=' + Database.password)
        return connect

