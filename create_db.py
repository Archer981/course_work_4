from flask import Flask
from setup_db import db
import json
from config import Config
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.user import User


app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()


with open('fixtures.json', encoding='utf-8') as file:
    data = json.load(file)

movies = [Movie(**movie) for movie in data['movies']]
genres = [Genre(**genre) for genre in data['genres']]
directors = [Director(**director) for director in data['directors']]
with db.session.begin():
    db.session.add_all(movies)
    db.session.add_all(genres)
    db.session.add_all(directors)
    db.session.commit()


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
