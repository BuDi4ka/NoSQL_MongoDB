from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField

class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
    tags = ListField(StringField())
