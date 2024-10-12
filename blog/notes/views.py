# notes/views.py
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , redirect
from django.urls import reverse, reverse_lazy
from .models import Post , Note
from .models import Author
from .forms import PostForm , NoteForm


def index(request):
    return HttpResponse("Hello from Notes app.")

def homepage2(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    notes = Note.objects.all()
    context = {'posts': posts, 'authors': authors, 'notes': notes}
    return render(request, 'notes/homepage2.html', context)



def add_post2(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_date = datetime.now()
            saved.update_date = datetime.now()

            saved.save()
            return HttpResponseRedirect(reverse_lazy('add_post'))

    return render(request,'notes/add_post2.html',{'form':form})

def post_detail2(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'notes/post_detail2.html', context)

def author_page2(request, pk):
    author = Author.objects.get(pk=pk)
    author_posts = Post.objects.filter(author=author)
    context = {'author': author , 'author_posts': author_posts}
    return render(request, 'notes/author_page2.html', context)

def add_like2(request, pk):
    post = Post.objects.get(pk=pk)
    post.number_of_likes+=1
    post.save()
    return render(request,'notes/post_detail2.html',{'post':post})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage2')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

def note_list(request): # Не правильно , але хай буде
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {'note': note}
    return render(request, 'notes/note_detail.html', context)