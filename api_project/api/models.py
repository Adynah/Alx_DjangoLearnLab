from django.db import models

# Models
class Book(models.Model):
    title =  models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
