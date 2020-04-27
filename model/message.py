from model.entity import Entity
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

    def __str__(self):
        return f"From: {self.from_user.username}, To: {self.to_user.username}, message: {self.context}"