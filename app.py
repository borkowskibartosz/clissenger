import argparse

from model.user import User
from model.message import Message
from service.user_service import UserService
from service.message_service import MessageService
from utils.db import connect_to_db

#add admins
#add list all messages for authorized user

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--authorize', help='authorize user', action='store_true')
    parser.add_argument('-c', '--add-user', help='add custom user', action='store_true')    
    parser.add_argument('-t', '--add-test-user', help='add test user', action='store_true')
    parser.add_argument('-l', '--list', help='list all users', action='store_true')
    parser.add_argument('-d', '--delete', help='remove selected user by username', action='store_true')
    parser.add_argument('-e', '--edit', help='update selected user by username', action='store_true')
    parser.add_argument('-u', '--username', help='user username')
    parser.add_argument('-p', '--password', help='user password')
    parser.add_argument('-n', '--new-password', help='user new password')
    parser.add_argument('-m', '--email', help='user email')
    parser.add_argument('-r', '--recipient', help='username of message recipient')
    parser.add_argument('-msg', '--message', help='message content')
    parser.add_argument('-s', '--send', help='send message', action='store_true')
    args = parser.parse_args() # parse all arguments

    connection = connect_to_db()
    if connection is None:
        print('Cannot connect to database')
        exit(-1)

    cursor = connection.cursor()

    if args.authorize == True:
        is_user_logged = UserService.login(cursor, args.username, args.password)
        if is_user_logged == True:
            print('Authorization done')
        else:
            print('Username or password invalid')

    if args.add_user == True and args.delete is not True and args.edit is not True:
        user = User()
        user.username = args.username
        user.email = args.email
        user.set_password(args.password, 'testowa-sol')
        user.save(cursor)
        print('Your user is created')

    if args.add_test_user == True:
        user = User()
        user.username = 'test'
        user.email = 'test@test.pl'
        user.set_password('qwerty12', 'testowa-sol')
        user.save(cursor)
        print(user)

    if args.list == True:
        print('List all users from database')
        users = UserService.get_all(cursor)
        for user in users:
            print(user)

    if args.delete == True:
        user = UserService.find_by_username(cursor, args.username)
        if user is not None:
            user.delete(cursor)
            print('User deleted')

    if args.edit == True:
        # Check is username and password authorize user
        if is_user_logged == True:
            user = UserService.find_by_username(cursor, args.username)
            user.set_password(args.new_password, 'testowa-sol')
            user.update(cursor)
            print('Password updated')
        else:
            print('Username or password invalid')        

    if args.send == True:
        is_recipient_exist = UserService.find_by_username(cursor, args.recipient)
        if is_user_logged == True and is_recipient_exist is not None:
            from_id = UserService.find_by_username(cursor, args.username)
            to_id = UserService.find_by_username(cursor, args.recipient)
            message = Message()
            message.from_user = from_id.id
            message.to_user = to_id.id
            message.context = args.message
            message.save(cursor)
            print("Message sent.")
        elif is_user_logged == True and is_recipient_exist is None:
            print(f'Recipient {args.recipient} doesn\'t exist')
        else:
            print('Please login to send a message')

    cursor.close()
    connection.close()