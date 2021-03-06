#from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# using js file
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Book
from .forms import albumForm, bookForm


# Create your views here.
#@login_required
def index(request):
  all_albums = Album.objects.all().order_by('title')
  return render(request, 'albums/list_albums.html', context={'albums':all_albums})
  

def add_albums(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        # message for JS fetch
        return JsonResponse({"deleted": 'true'})
        # django commands
        # return redirect(to='list_albums')
    # return render(request, "albums/delete_albums.html", {"album": album})


def albums_detail(request, pk):
  album = get_object_or_404(Album, pk=pk)
  return render(request, "albums/albums_detail.html", {"album": album})


# def add_details(request, pk):
#     albums = get_object_or_404(Album, pk=pk)
#     if request.method == 'GET':
#         form = DetailForm()
#     else:
#         form = DetailForm(data=request.POST)
#         if form.is_valid():
#             new_details = form.save(commit=False)
#             new_details.albums = albums
#             new_details.save()
#             return redirect(to='list_albums', pk=pk)

#     return render(request, "albums/add_details.html", {"form": form, "albums": albums})


def edit_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = albumForm(instance=album)
    else:
        form = albumForm(data=request.POST, instance=album)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_albums.html", {
        "form": form, "album": album})


# BOOK COMMANDS
def book_index(request):
  books = Book.objects.all().order_by('author')
  return render(request, 'books/home.html', context={'books':books})