import sys
from models import Author, Quote

def name_select(*args):
    author = Author.objects(fullname=args).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(f"Quote: {quote.quote}, Author: {quote.author.fullname}")
    else:
        print('Author not found')

def tag_select(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(f"Quote: {quote.quote}, Author: {quote.author.fullname}")

def tags_select(tags):
    for tag in tags.split(','):
        tag_select(tag.strip())

def parse_input(user_input):
    cmd, *args = user_input.split(':')
    cmd = cmd.strip().lower()
    args = ':'.join(args).strip().split(',')
    return cmd, args

def select_db():
    while True:
        user_input = input('Enter command - ')
        cmd, args = parse_input(user_input)

        if cmd == 'exit':
            sys.exit(0)
        elif cmd == 'name':
            name_select(*args)
        elif cmd == 'tags':
            tags_select(*args)
        elif cmd == 'tag':
            tag_select(args)
        else:
            print('Invalid command')



