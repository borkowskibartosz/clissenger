from model.user import User
from service.password_service import check_password

class UserService:
    @staticmethod
    def login(cursor, username, password):
        user = UserService.find_by_username(cursor, username)
        if user is None:
            return None
        return check_password(password, user.hashed_password)


    @staticmethod
    def find_by_id(cursor, user_id):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user._id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user._hashed_password = data[3]
            return loaded_user
        else:
            return None
    
    @staticmethod
    def find_by_username(cursor, username):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE username=%s"
        cursor.execute(sql, (username,))
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user._id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user._hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def get_all(cursor):
        sql = "SELECT id, username, email, hashed_password FROM users"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_user = User()
            loaded_user._id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user._hashed_password = row[3]
            ret.append(loaded_user)
        return ret
