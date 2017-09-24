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


    @staticmethod
    def all():
        try:
            db = DbController(os.path.join(os.getcwd(), '..', 'db'), 'post')
            posts = db.all()
            user_list = []
            db = DbController(os.path.join(os.getcwd(), '..', 'db'), 'p_files')
            for data in posts:
                file_list = [i['Id'] for i in db.all(param_name='post_id', param_value=data['Id'])]
                user_list.append(Post(data['Id'], data['title'], data['text'], data['owner'], file_list))
            return user_list
        except sqlite3.Error as e:
            print(e)
        return None

    def update(self):
        try:
            self.__db.update(self._id, title=self.title, text=self.text, owner= self.owner)
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete(self):
        try:
            self.__db.delete(self._id)
            return True
        except sqlite3.Error as e:
            print(e)
            return False
