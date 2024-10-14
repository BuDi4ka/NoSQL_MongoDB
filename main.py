import sys
import db_connection
from query import name_select, tag_select, tags_select, parse_input

def select_db():
    while True:
        user_input = input('Enter command (or "exit" to exit): ')
        if user_input.strip().lower() == 'exit':
            print("Exiting...")
            sys.exit(0)
        cmd, args = parse_input(user_input)

        if cmd == 'name':
            name_select(args)
        elif cmd == 'tag':
            tag_select(args)
        elif cmd == 'tags':
            tags_select(args)
        else:
            print('Unknown command, try again.')

if __name__ == "__main__":
    select_db()
