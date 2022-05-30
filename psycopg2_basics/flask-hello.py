from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus as urlquote

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@127.0.0.1:5432/test' % urlquote(
    'theceo@16')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return ("Hello " + person.name)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
