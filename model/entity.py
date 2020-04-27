class Entity:
    def save(self, cursor):
        raise NotImplementedError

    def update(self, cursor):
        raise NotImplementedError

    def delete(self, cursor):
        raise NotImplementedError
