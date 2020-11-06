import mysql.connector as conn


def conn_db():
    return conn.connect(host='localhost',
                        user='root',
                        password='',
                        database='bloger'
                        )
