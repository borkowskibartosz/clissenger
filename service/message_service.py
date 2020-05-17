from model.message import Message


class MessageService:
    #repair !!!
    # @staticmethod
    # def send_to_user(cursor, message, username):
    #     message = MessageService.find_by_recipient(cursor, username)
    #     if username is None:
    #         return None
    #     else:
    #         return True

    @staticmethod
    def get_all(cursor, username):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages;"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message._id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.context = row[3]
            loaded_message.created_at = row[4]
            ret.append(loaded_message)
        return ret


    @staticmethod
    def find_by_id(cursor, message_id):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE id=%s;"
        cursor.execute(sql, (message_id,))
        data = cursor.fetchone()
        if data:
            loaded_message = Message()
            loaded_message._id = data[0]
            loaded_message.from_user = data[1]
            loaded_message.to_user = data[2]
            loaded_message.context = data[3]
            loaded_message.created_at = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def find_by_recipient(cursor, recipient_username):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE to_user=%s;"
        cursor.execute(sql, (recipient_username,))
        data = cursor.fetchone()
        if data:
            loaded_message = Message()
            loaded_message._id = data[0]
            loaded_message.from_user = data[1]
            loaded_message.to_user = data[2]
            loaded_message.context = data[3]
            loaded_message.created_at = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def delete_all(cursor):
        sql = "DELETE FROM messages"
        cursor.execute(sql)

    # TODO: Create message service with methods:
    # - send_to_user(cursor, message, username)
    # - get_all(cursor, username)
    # - find_by_id(cursor, message_id)
    # - find_by_recipient(cursor, recipient_username)