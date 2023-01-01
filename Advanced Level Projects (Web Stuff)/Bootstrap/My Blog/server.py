from flask import Flask, render_template, request, flash
from smtplib import *
import requests
import os

app = Flask(__name__)


@app.route('/index')
def index():
    blog_url = os.environ.get('URL')
    response = requests.get(blog_url)
    all_blogs = response.json()
    return render_template('index.html', blogs=all_blogs)


@app.route('/contact')
def contact():
    return render_template('contact.html', message='')


@app.route('/send', methods=['POST', 'GET'])
def send():
    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("PASSWORD")
    print(my_email)
    print(password)
    name = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone_number']
    msg = request.form['msg']
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='maniyarkaushal111@gmail.com',
            msg=f'Subject:Message from Reader\n\nName: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {msg}')
        return render_template('contact.html', message="Your Message is Delivered")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<int:id_wanted>')
def post(id_wanted):
    blog_url = os.environ.get('URL')
    response = requests.get(blog_url)
    all_blogs = response.json()
    for blog in all_blogs:
        if blog['id'] == id_wanted:
            req_blog = blog
    return render_template('post.html', blog=req_blog)


if __name__ == '__main__':
    app.run(debug=True)
