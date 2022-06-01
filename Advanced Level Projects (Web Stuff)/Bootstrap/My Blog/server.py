from flask import Flask, render_template
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
    return render_template('contact.html')


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
