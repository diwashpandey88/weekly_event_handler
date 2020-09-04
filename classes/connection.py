import mysql.connector

class DataBase:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user = 'root', password = "", host = "localhost", port=3306, database ="weekly event handler")
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def insert_with_id_return(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def show_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    def show_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data
DataBase()