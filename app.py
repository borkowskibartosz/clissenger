import argparse

from model.user import User
from service.user_service import UserService
from utils.db import connect_to_db


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

    if args.add_user == True:
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
        print('User created')

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
        # UserService.login(cursor, args.username, args.password)
        # If user logged then set new password from args.new_password
        # user.update(cursor)
        pass

    cursor.close()
    connection.close()