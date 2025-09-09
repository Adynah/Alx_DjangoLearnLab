from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

# Expected Output:
# 1984  ← if __str__ is defined
# (otherwise: Book object (2))