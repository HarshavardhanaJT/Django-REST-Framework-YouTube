from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.

class BookView(APIView):

    def get(self, request):
        data = {}
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            data['status'] = True
            data['books'] = serializer.data

        except Exception as e:
            data['status'] = False
            data['message'] = "Oops something went wrong"

        return Response(data=data)

    def post(self, request):
        data = {}
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data['status'] = True
                data['message'] = "Data saved successfully"
            else:
                data['status'] = False
                data['message'] = "Invalid data"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to save the data"

        return Response(data=data)

    def put(self, request):
        data = {}
        try:
            book = Book.objects.get(id=request.data.get("id"))
            serializer = BookSerializer(book, request.data)
            if serializer.is_valid():
                serializer.save()
                data['status'] = True
                data['message'] = "Data updated successfully"
            else:
                data['status'] = False
                data['message'] = "Invalid data"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to update the data"

        return Response(data=data)

    
    def delete(self, request):
        data = {}
        try:
            book = Book.objects.get(id=request.query_params.get("id"))
            book.delete()
            data['status'] = True
            data['message'] = "Book deleted successfully"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to delete book"

        return Response(data=data)