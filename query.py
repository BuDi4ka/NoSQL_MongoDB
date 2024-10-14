from models import Author, Quote

def name_select(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        if quotes:
            for quote in quotes:
                print(f"{quote.quote}")
        else:
            print(f"No quotes from - {author_name}")
    else:
        print('Author not found')

def tag_select(tag):
    quotes = Quote.objects(tags=tag)
    if quotes:
        for quote in quotes:
            print(f"{quote.quote} - {quote.author.fullname}")
    else:
        print(f"No quotes with tag - {tag}")

def tags_select(tags):
    tag_list = [tag.strip() for tag in tags.split(',')]
    quotes = Quote.objects(tags__in=tag_list)
    if quotes:
        for quote in quotes:
            print(f"{quote.quote} - {quote.author.fullname}")
    else:
        print(f"No quotes with tags - {', '.join(tag_list)}")

def parse_input(user_input):
    cmd, *args = user_input.split(':', 1)
    cmd = cmd.strip().lower()
    args = args[0].strip() if args else ''
    return cmd, args


