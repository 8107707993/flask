# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="bloger"
# )
#
# mycursor = mydb.cursor()
#
#
# sql = "INSERT INTO contacts(name, msg) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
# exit()
# from flask import Flask
# from flask_sqlalchemy import *
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/bloger'
# db = SQLAlchemy(app)
#
#
# class Contacts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String, unique=True, nullable=False)
#
#
# db.session.add(Contacts(username="Flask", email="example@example.com"))
# db.session.commit()
#
# users = Contacts.query.all()
#
# exit()
#
# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# admin = User('admin', 'admin@example.com')
#
# db.session.add(admin)
#
# User.query.all()
#
# User.query.filter_by(username='admin').first()

from flask import Flask, render_template, request, jsonify, abort as ab
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector as conn

app = Flask(__name__)


def conn_db():
    return conn.connect(host='localhost',
                        user='root',
                        password='',
                        database='bloger'
                        )


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''add entry to the database'''

        def add_data():
            cnx = conn_db()
            cursor = cnx.cursor()
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            date=datetime.now()
            # if not request.json:
            #     ab(400)

            cursor.execute("INSERT INTO contacts(name,phone_num, msg , email,date) VALUES (%s,%s, %s, %s, %s)",
                           (name, phone, message, email,date))
            cnx.commit()

        add_data()

    return render_template('contact.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
