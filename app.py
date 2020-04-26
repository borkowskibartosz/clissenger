import argparse
from utils.db import connect_to_db

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='list all users', action='store_true')
    parser.add_argument('-d', '--delete', help='remove selected user by username', action='store_true')
    parser.add_argument('-e', '--edit', help='update selected user by username', action='store_true')
    parser.add_argument('-u', '--username', help='user username')
    parser.add_argument('-p', '--password', help='user password')
    parser.add_argument('-n', '--new-password', help='user new password')
    args = parser.parse_args() # parse all arguments

    connection = connect_to_db()
    if connection is None:
        print('Cannot connect to database')
        exit(-1)

    cursor = connection.cursor()

    print(args)

    if args.list == True:
        print("List all users from database")

    cursor.close()
    connection.close()