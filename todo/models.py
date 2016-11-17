from django.db import models

# Create your models here.
# the following lines added:


class Todo(models.Model):
    index = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.index + ' ' + self.content

