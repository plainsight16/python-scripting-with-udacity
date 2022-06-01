import sys
from flask import Flask, abort, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from urllib.parse import quote_plus as urlquote

from sqlalchemy import PrimaryKeyConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/todoapp' % urlquote(
    'theceo@16')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f'<Todo ID: {self.id} Description: {self.description}>'


@app.route('/')
def index():
    todo_items = db.session.query(Todo).all()

    return render_template('index.html', data=todo_items)


@app.route('/todo/create', methods=['GET', 'POST'])
def create_todo():
    if request.method == 'POST':
        error = False
        body = {}
        try:
            desc = request.get_json()['description']
            new_todo = Todo(description2=desc)
            db.session.add(new_todo)
            db.session.commit()
            body['description'] = new_todo.description
        except:
            db.session.rollback()
            print(sys.exc_info())
            error = True
        finally:
            db.session.close()

        if error:
            abort(400)
        else:
            return jsonify(body)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
