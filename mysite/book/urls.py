from django.urls import path
from .views import BookView

"""
YouTube : CodingWithHarsha
Web Application(made using Python, Django REST Framework and Angular 10) : codingwithharsha.in

"""

urlpatterns = [
    path('books/', BookView.as_view()),
]