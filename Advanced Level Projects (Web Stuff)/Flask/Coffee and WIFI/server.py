import wtforms
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap(app)

COFFEE_RATING = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
WIFI_STRENGTH = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER_AVAILABILITY = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Loacation on Google Map', validators=[DataRequired()])
    open = StringField('Opening Time', validators=[DataRequired()])
    close = StringField('Closing Time', validators=[DataRequired()])
    coffee = wtforms.SelectField('Coffee Rating', validators=[DataRequired()], choices=COFFEE_RATING)
    wifi = wtforms.SelectField('WIFI Rating', validators=[DataRequired()], choices=WIFI_STRENGTH)
    power = wtforms.SelectField('Power Socket Availability', validators=[DataRequired()], choices=POWER_AVAILABILITY)
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        details = [cafe_form.cafe.data, cafe_form.location.data, cafe_form.open.data, cafe_form.close.data,
                   cafe_form.coffee.data, cafe_form.wifi.data, cafe_form.power.data]
        with open('cafe-data.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(details)
            f.close()
    return render_template('add.html', form=cafe_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv',newline='' ,  encoding='UTF-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            if row!=[]:
                list_of_rows.append(row)
    table_headings = list_of_rows[0]
    list_of_rows.pop(0)
    return render_template('cafes.html', cafes=list_of_rows, heading=table_headings)


if __name__ == '__main__':
    app.run(debug=True)
