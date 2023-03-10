from flask import current_app
from sqlalchemy import desc
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_new(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def get_all_paginate(self, page):
        return self.session.query(Movie).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'],
                                                  error_out=False)

    def get_all_new_paginate(self, page):
        return self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()
