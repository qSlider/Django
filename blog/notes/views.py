# notes/views.py
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , redirect
from django.urls import reverse, reverse_lazy
from .models import Post, Note, Author, Category
from .forms import PostForm , NoteForm


def index(request):
    return HttpResponse("Hello from Notes app.")


def homepage2(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    notes = Note.objects.all()
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    reminder_date_filter = request.GET.get('reminder_date', '')
    reminder_time_filter = request.GET.get('reminder_time', '')

    if search_query:
        notes = notes.filter(title__icontains=search_query)

    if category_filter:
        notes = notes.filter(category__title=category_filter)

    if reminder_date_filter:
        try:
            reminder_date = datetime.strptime(reminder_date_filter, '%Y-%m-%d')
            notes = notes.filter(reminder__date=reminder_date)
        except ValueError:
            pass

    if reminder_time_filter:
        try:
            reminder_time = datetime.strptime(reminder_time_filter, '%H:%M').time()
            notes = notes.filter(reminder__hour=reminder_time.hour, reminder__minute=reminder_time.minute)
        except ValueError:
            pass

    context = {
        'posts': posts,
        'authors': authors,
        'notes': notes,
        'categories': categories,
    }
    return render(request, 'notes/homepage2.html', context)

def homepagetest(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    notes = Note.objects.all()
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    reminder_date_filter = request.GET.get('reminder_date', '')
    reminder_time_filter = request.GET.get('reminder_time', '')

    if search_query:
        notes = notes.filter(title__icontains=search_query)

    if category_filter:
        notes = notes.filter(category__title=category_filter)

    if reminder_date_filter:
        try:
            reminder_date = datetime.strptime(reminder_date_filter, '%Y-%m-%d')
            notes = notes.filter(reminder__date=reminder_date)
        except ValueError:
            pass

    if reminder_time_filter:
        try:
            reminder_time = datetime.strptime(reminder_time_filter, '%H:%M').time()
            notes = notes.filter(reminder__hour=reminder_time.hour, reminder__minute=reminder_time.minute)
        except ValueError:
            pass

    context = {
        'posts': posts,
        'authors': authors,
        'notes': notes,
        'categories': categories,
    }
    return render(request, 'notes/homepagetest.html', context)



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

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'notes/delete_note.html', {'note': note})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})
