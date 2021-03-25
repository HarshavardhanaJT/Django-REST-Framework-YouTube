from django.db import models

# Create your models here.

"""
YouTube : CodingWithHarsha
Web Application(made using Python, Django REST Framework and Angular 10) : codingwithharsha.in

"""

class Book(models.Model):

    name = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name