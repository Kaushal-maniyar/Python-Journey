from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(10), nullable=False)


db.create_all()
Bootstrap(app)
all_books = db.session.query(Book).all()


class AddBook(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField(label='Add')


class RatingForm(FlaskForm):
    rating = rating = StringField('New Rating', validators=[DataRequired()])
    submit = SubmitField(label='Edit')


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books, len=len(all_books))


@app.route("/add", methods=['POST', 'GET'])
def add():
    add_book = AddBook()
    if add_book.validate_on_submit():
        details = {
            'title': add_book.name.data,
            'author': add_book.author.data,
            'rating': add_book.rating.data
             }
        new_book = Book(title=details['title'], author=details['author'], rating=details['rating'])
        db.session.add(new_book)
        db.session.commit()
        all_books.append(details)
    return render_template('add.html', form=add_book)


@app.route('/edit_rating', methods=['POST', 'GET'])
def edit():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    rating_form = RatingForm()
    if rating_form.validate_on_submit():
        book.rating = rating_form.rating.data
        db.session.commit()
    return render_template('edit_rating.html', form=rating_form, name=book.title, rating=book.rating)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

