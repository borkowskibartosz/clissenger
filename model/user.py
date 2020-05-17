from model.entity import Entity
from service.password_service import password_hash

class User(Entity):
    _id = None
    _hashed_password = None
    username = None
    email = None

    def __init__(self):
        self._id = -1
        self._hashed_password = ''
        self.username = ''
        self.email = ''

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt):
        self._hashed_password = password_hash(password, salt)

    def save(self, cursor):
        if not self._id == -1:
            return False

        sql = """INSERT INTO users(username, email, hashed_password)
                VALUES(%s, %s, %s) RETURNING id"""
        values = (self.username, self.email, self.hashed_password)
        cursor.execute(sql, values)
        self._id = cursor.fetchone()[0]  # albo cursor.fetchone()['id']
        return True

    def update(self, cursor):
        if self._id == -1:
            return False
        
        sql = """UPDATE users SET username=%s, email=%s, hashed_password=%s WHERE id=%s"""
        values = (self.username, self.email, self.hashed_password, self.id)
        cursor.execute(sql, values)
        return True

    def delete(self, cursor):
        if self._id == -1:
            return False

        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, (self.id,))
        self._id = -1
        return True

    def __str__(self):
        return f"ID: {self.id}, username: {self.username}, e-mail: {self.email}"
