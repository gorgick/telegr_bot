import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user):
        with self.connection:
            result = self.cursor.execute("select * from mainapp_owner where username == ?", (user,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user):
        with self.connection:
            return self.cursor.execute("insert into mainapp_owner (username) values (?)", (user,))

    def create_notification(self, user, text):
        with self.connection:
            admin = self.cursor.execute("select id from auth_user where username = 'admin'").fetchone()
            user_id = self.cursor.execute("select id from mainapp_owner where username == ?", (user,)).fetchone()
            print(admin, user_id)
            if admin and user_id:
                return self.cursor.execute(
                    "insert into mainapp_notification (reciever_id, user_id, text) values (?, ?, ?) ",
                    (admin[0], user_id[0], text))
