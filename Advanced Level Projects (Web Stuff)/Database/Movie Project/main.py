from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

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
    title = StringField('Movie Name', validators=[DataRequired()])
    year = StringField('Year of Release', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = StringField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    print(all_movies)
    all_movies = sorted(all_movies, key=lambda x: x.ranking, reverse=True)
    return render_template("index.html", movies=all_movies, len=len(all_movies))


@app.route("/add", methods=['POST', 'GET'])
def add():
    add_movie = MovieForm()
    if add_movie.validate_on_submit():
        details = {
            'title': add_movie.title.data,
            'year': add_movie.year.data,
            'description': add_movie.description.data,
            'rating': add_movie.rating.data,
            'ranking': add_movie.ranking.data,
            'review': add_movie.review.data,
            'img_url': add_movie.img_url.data
        }
        new_movie = Movie(title=details['title'], year=details['year'], description=details['description'],
                          rating=details['rating'], ranking=details['ranking'], review=details['review'],
                          img_url=details['img_url'])
        db.session.add(new_movie)
        db.session.commit()
        return render_template('message.html', message="Movie Added Successfully")
    return render_template("add.html", form=add_movie)


@app.route('/update', methods=['POST', 'GET'])
def edit():
    movie_id = request.args.get('movie_id')
    movie = Movie.query.get(movie_id)
    edit_movie = MovieForm(title=movie.title, year=movie.year, description=movie.description, rating=movie.rating,
                           ranking=movie.ranking, review=movie.review, img_url=movie.img_url)
    if edit_movie.validate_on_submit():
        movie.title = edit_movie.title.data
        movie.year = edit_movie.year.data
        movie.description = edit_movie.description.data
        movie.rating = edit_movie.rating.data
        movie.ranking = edit_movie.ranking.data
        movie.review = edit_movie.review.data
        movie.img_url = edit_movie.img_url.data
        db.session.commit()
        return render_template('message.html', message="Updated Successfully")
    return render_template('edit.html', form=edit_movie)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('movie_id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
