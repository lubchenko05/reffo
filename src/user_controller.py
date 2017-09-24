import os
import sqlite3

from db_controller import DbController


class User:
    def __init__(self, id_, username, password):
        self._id = id_
        self.password = password
        self.username = username
        self.__db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'user')

    @staticmethod
    def registration(username, password):
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'user')
            id_ = db.create(username=username, password=password)
            return User(id_, username, password)
        except sqlite3.Error as e:
            print(e)
        return None


    def verify(self):
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'user')
            id_ = db.query(f'SELECT id from user WHERE user_name=\'{self.username}\' and password=\'{self.password}\';')
            if id_:
                return True
        except sqlite3.Error as e:
            print(e)
        return False

    @staticmethod
    def get_user(username):
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db'), 'user')
            data = db.get('username', username)
            if not data:
                return None
            return User(data['Id'], data['username'], data['password'])
        except sqlite3.Error as e:
            print(e)
        return None

    @staticmethod
    def all_user():
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db'), 'user')
            users = db.all()
            user_list = []
            for data in users:
                user_list.append(User(data['Id'], data['username'], data['password']))
            return user_list
        except sqlite3.Error as e:
            print(e)
        return None

    def update(self):
        try:
            self.__db.update(self._id, username = self.username, password= self.password)
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete_user(self):
        try:
            self.__db.delete(self._id)
            return True
        except sqlite3.Error as e:
            print(e)
            return False
