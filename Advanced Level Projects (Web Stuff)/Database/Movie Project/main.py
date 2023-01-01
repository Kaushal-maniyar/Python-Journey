from flask import Flask, render_template, redirect, url_for, request
# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
# Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(800))


class MovieForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    year = StringField('Year of Release', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = StringField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])


db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['POST', 'GET'])
def add():
    add_book = MovieForm()
    if add_book.validate_on_submit():
        new_movie = Movie()
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)
