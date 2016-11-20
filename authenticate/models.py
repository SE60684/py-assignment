from mongoengine import *
# Create your models here.
# the following lines added:


class User(DynamicDocument):
    username = StringField(max_length=200, required=True)
    password = StringField(max_length=200, required=True)


