from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from .models import Book

def index(request):
    return HttpResponse("Hello World")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html',{'book':book})
    #return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")