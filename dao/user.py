from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("email"))
        user.name = user_d.get("name", user.name)
        user.surname = user_d.get('surname', user.surname)
        user.favorite_genre = user_d.get('favorite_genre', user.favorite_genre)
        self.session.add(user)
        self.session.commit()

    def update_password(self, user_d):
        user = self.get_one(user_d.get("email"))
        user.password = user_d.get("password_2", user.password)
        self.session.add(user)
        self.session.commit()
