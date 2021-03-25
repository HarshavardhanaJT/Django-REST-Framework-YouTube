from rest_framework import serializers
from .models import Book

"""
YouTube : CodingWithHarsha
Web Application(made using Python, Django REST Framework and Angular 10) : codingwithharsha.in

"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # fields = ['id','name','isbn','author','publish_year']
        fields = "__all__"