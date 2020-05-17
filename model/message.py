from model.entity import Entity
from model.user import User
from datetime import datetime

# TODO: Same as user entity with methods: save, update and delete
class Message(Entity):
    _id = None
    from_user = None
    to_user = None 
    context = None
    created_at = None

    def __init__(self):
        self._id = -1
        self.from_user = User()
        self.to_user = User()
        self.context = ''
        self.created_at = datetime.now()

    @property
    def id(self):
        return self._id

    def save(self, cursor):
        if not self._id == -1:
            return False
        sql = """INSERT INTO messages(from_user, to_user, context, created_at) 
                VALUES(%s, %s, %s, NOW()) RETURNING id;"""
        values = (self.from_user, self.to_user, self.context)
        cursor.execute(sql, values)
        return True
        
    def update(self, cursor):
        if self._id == -1:
            return False
        
        sql = """UPDATE messages SET from_user=%s, to_user=%s, context=%s WHERE id=%s"""
        values = (self.from_user, self.to_user, self.context, self.id)
        cursor.execute(sql, values)
        return True

    def delete(self, cursor):
        if self._id == -1:
            return False

        sql = "DELETE FROM messages WHERE id=%s"
        cursor.execute(sql, (self.id,))
        self._id = -1
        return True

    def __str__(self):
        return f"From: {self.from_user.username}, To: {self.to_user.username}, message: {self.context}"