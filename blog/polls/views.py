from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post
from .models import Author
from .forms import PostForm



def homepage(request):
    posts = Post.objects.all()
    author = Author.objects.all()
    context = {'posts': posts ,'author':author}
    return render(request, 'polls/homepage.html' , context)

def index(request):
    notes = ['Note 1', 'Note 2', 'Note 3']
    return render(request, 'polls/index.html', {'notes': notes})

def add_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_date = datetime.now()
            saved.update_date = datetime.now()

            saved.save()
            return HttpResponseRedirect(reverse_lazy('add_post'))

    return render(request,'polls/add_post.html',{'form':form})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'polls/post_detail.html', context)

def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    author_posts = Post.objects.filter(author=author)
    context = {'author': author , 'author_posts': author_posts}
    return render(request, 'polls/author_page.html', context)

def add_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.number_of_likes+=1
    post.save()
    return render(request,'polls/post_detail.html',{'post':post})