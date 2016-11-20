from django.db import models
from mongoengine import *
# Create your models here.
# the following lines added:


# class ABC(models.Model):
#     index = models.CharField(max_length=200)
#     content = models.CharField(max_length=200)
#
#     def __str__(self):
#         return str(self.id) + ' ' + self.index + ' ' + self.content


class Todo(DynamicDocument):
    index = StringField(max_length=200, required=True)
    content = StringField(max_length=200, required=True)
    uid = LongField(required=True)
