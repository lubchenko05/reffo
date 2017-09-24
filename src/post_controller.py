import os
import sqlite3

from db_controller import DbController


class Post:
    def __init__(self, id_, title, text, owner, files):
        self._id = id_
        self.title = title
        self.text = text
        self.owner = owner
        self.files = files
        self.__db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'post')

    @staticmethod
    def create(title, text, owner, files):
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'post')
            post_id = db.create(title, text, owner)
            db = DbController(os.path.join(os.getcwd(), '..', 'db.sqlite3'), 'p_files')
            post_files = []
            if files:
                for i in files:
                    try:
                        id_ = db.create(i[0], post_id, i[1], i[2])
                        post_files.append(id_)
                    except:
                        continue
            return Post(post_id, title, text, owner, post_files)
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
