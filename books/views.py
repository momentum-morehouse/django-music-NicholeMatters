from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import bookForm

# Create your views here.
def book_index(request):
  books = Book.objects.all().order_by('author')
  return render(request, 'books/book_index.html', context={'books': books})

  
def add_book(request):
    if request.method == 'GET':
        form = bookForm()
    else:
        form = bookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='book_index')

    return render(request, "books/add_book.html", {"form": form})

