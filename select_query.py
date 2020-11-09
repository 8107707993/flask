import mysql.connector as conn


def conn_db():
    return conn.connect(host='localhost',
                        user='root',
                        password='',
                        database='bloger'
                        )

    cursor = conn.connect()

    query = "SELECT title FROM posts"

    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)



