import json
import mysql.connector as mysql
from datetime import datetime
from flask import Flask, render_template, request
import conn
import select_query as sel
from flask_sqlalchemy import SQLAlchemy

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)


# class Posts:
#     def title(self, records):
#         cursor = conn.conn_db().cursor()
#         query = params['post_title'],
#         cursor.execute(query)
#         records = cursor.fetchall()
#         for record in records:
#             print(record)
#         cursor.close()
#
#     def tagline(self, query):
#         cursor = conn.conn_db().cursor()
#         query1 = params['post_tagline'],
#         cursor.execute(query1)
#         records1 = cursor.fetchall()
#         for record in records1:
#             print(record)
#         cursor.close()
#
#     def img_file(self, query):
#         cursor = conn.conn_db().cursor()
#         query2 = params['post_img_file'],
#         cursor.execute(query2)
#         records2 = cursor.fetchall()
#         for record in records2:
#             print(record)
#         cursor.close()
#
#     def slug(self, query):
#         cursor = conn.conn_db().cursor()
#         query3 = params['post_slug'],
#         cursor.execute(query3)
#         records3 = cursor.fetchall()
#         for record in records3:
#             print(record)
#         cursor.close()
#
#     def content(self, query):
#         cursor = conn.conn_db().cursor()
#         query4 = params['post_content'],
#         cursor.execute(query4)
#         records4 = cursor.fetchall()
#         for record in records4:
#             print(record)
#
#         cursor.close()
#
#     def date(self, query):
#         cursor = conn.conn_db().cursor()
#         query5 = params['post_date'],
#         cursor.execute(query5)
#         records5 = cursor.fetchall()
#         for record in records5:
#             print(record)
#         cursor.close()


@app.route('/')
def home():
    post = sel.conn_db()
    # po_data = Posts.title().query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html', params=params, post=post)


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

            cursor.execute("INSERT INTO contacts(name,phone_num, msg , email,date) VALUES (%s,%s, %s, %s, %s)",
                           (name, phone, message, email, date))
            cnx.commit()
            cursor.close()

        add_data()

    return render_template('contact.html')


@app.route('/post', methods=['GET'])
def post_route(post_slug):

    # po_slug = Posts.query.filter_by(slug=params['post_slug']).first()
    return render_template('post.html', params=params, post=params['post_title'])


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
