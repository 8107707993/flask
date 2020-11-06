import json

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import conn

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

# app.config.update(
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT='465',
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=params['user-mail'],
#     MAIL_PASSWORD=params['user-password']
# )
#
# mail = Mail(app)

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


conn.conn_db()


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''add entry to the database'''

        def add_data():
            cnx = conn.conn_db()
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
            # mail.send_message('New message from ' + name,
            #                   sender=email,
            #                   recipients=[params['user-mail']],
            #                   body=message + "\n" + phone
            #                   )

        add_data()

    return render_template('contact.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
