from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector as conn

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bloger'
# db = SQLAlchemy(app)

#
# class Contacts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)


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
    if (request.method == 'post'):
        '''add entry to the database'''

        def add_data():
            cnx = conn_db()
            cursor = cnx.cursor()
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            date = datetime.now()
            # if not request.json:
            #     ab(400)

            cursor.execute("INSERT INTO contacts(name,phone_num, msg , email,date) VALUES (%s,%s, %s, %s, %s)",
                           (name, phone, message, email, date))
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
