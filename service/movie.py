from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        movie = self.dao.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title", movie.title)
        movie.description = movie_d.get("description", movie.description)
        movie.trailer = movie_d.get("trailer", movie.trailer)
        movie.year = movie_d.get("year", movie.year)
        movie.rating = movie_d.get("rating", movie.rating)
        movie.genre_id = movie_d.get("genre_id", movie.genre_id)
        movie.director_id = movie_d.get("director_id", movie.director_id)

        self.dao.update(movie)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
